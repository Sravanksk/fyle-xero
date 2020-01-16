import json
import ast
from dateutil.parser import parse

from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from apps.expense.models import ExpenseGroup, Expense
from apps.xero_workspace.models import Workspace, CategoryMapping
from apps.task.models import TaskLog
from apps.task.tasks import create_task


class ExpenseGroupView(View):
    """
    Expense Group View
    """
    template_name = "expense/expense_group.html"

    def get(self, request, workspace_id):
        """
        Render expense group screen with necessary fields
        :param request
        :param workspace_id
        :return: render expense groups screen
        """
        expense_groups_details = []
        expense_groups = ExpenseGroup.objects.filter(
            workspace=Workspace.objects.get(id=workspace_id)
        )

        for expense_group in expense_groups:
            serialized_expense_group = json.loads(serializers.serialize('json', [expense_group]))
            expense_group_fields = {k: v for d in serialized_expense_group for k, v in d.items()}["fields"]
            expense_group_fields["id"] = expense_group.id
            expense_group_fields["description"] = json.loads(expense_group_fields["description"])
            expense_group_fields["description"]["approved_at"] = parse(
                expense_group_fields["description"]["approved_at"])
            expense_group_fields["status"] = TaskLog.objects.filter(
                expense_group=expense_group).first().task.success
            expense_groups_details.append(expense_group_fields)

        page = request.GET.get('page', 1)
        paginator = Paginator(expense_groups_details, 10)
        try:
            expense_groups_details = paginator.page(page)
        except PageNotAnInteger:
            expense_groups_details = paginator.page(1)
        except EmptyPage:
            expense_groups_details = paginator.page(paginator.num_pages)

        context = {"expense_groups_tab": "active", "expense_groups": "active",
                   "expense_groups_details": expense_groups_details}
        return render(request, self.template_name, context)

    def post(self, request, workspace_id):
        value = request.POST.get('submit')
        selected_expense_group_id = [ast.literal_eval(x) for x in request.POST.getlist('expense_group_ids')]
        if value == 'resync' and len(selected_expense_group_id) > 0:
            for expense_group_id in selected_expense_group_id:
                create_task(workspace_id, expense_group_id)
        return HttpResponseRedirect(self.request.path_info)


class ExpenseView(View):
    """
    Expense View
    """
    template_name = "expense/expense.html"

    def get(self, request, workspace_id, group_id):
        """
        Render expenses screen with necessary fields
        :param request
        :param workspace_id
        :param group_id
        :return: render expenses screen
        """
        expense_group = ExpenseGroup.objects.get(id=group_id)
        report_id = json.loads(expense_group.description)["report_id"]
        expense_group_id = expense_group.id
        expenses = expense_group.expenses.all()

        page = request.GET.get('page', 1)
        paginator = Paginator(expenses, 10)
        try:
            expenses = paginator.page(page)
        except PageNotAnInteger:
            expenses = paginator.page(1)
        except EmptyPage:
            expenses = paginator.page(paginator.num_pages)

        context = {"expense_groups_tab": "active", "expenses": expenses,
                   "report_id": report_id, "expense_group_id": expense_group_id}
        return render(request, self.template_name, context)


class ExpenseDetailsView(View):
    """
    Expense details view
    """

    @staticmethod
    def get(request, workspace_id, group_id, expense_id):
        """
        Return fields for expense details modal
        :param request
        :param workspace_id
        :param group_id
        :param expense_id
        :return: expense fields JSON
        """
        expense = Expense.objects.get(id=expense_id)
        serialized_expense = json.loads(serializers.serialize('json', [expense]))
        expense_fields = {k: v for d in serialized_expense for k, v in d.items()}["fields"]
        expense_fields["category_code"] = CategoryMapping.objects.get(
            workspace__id=workspace_id, category=expense_fields["category"]).account_code
        expense_fields["expense_created_at"] = parse(expense_fields["expense_created_at"]).strftime(
            '%b. %d, %Y, %-I:%M %-p')
        expense_fields["spent_at"] = parse(expense_fields["spent_at"]).strftime(
            '%b. %d, %Y, %-I:%M %-p')
        return JsonResponse(expense_fields)


class InvoiceDetailsView(View):
    """
    Invoice details view
    """

    @staticmethod
    def get(request, workspace_id, group_id):
        """
        Return fields for invoice details modal
        :param request
        :param workspace_id
        :param group_id
        :return: invoice fields JSON
        """
        invoice = ExpenseGroup.objects.get(id=group_id).invoice
        serialized_invoice = json.loads(serializers.serialize('json', [invoice]))
        invoice_fields = {k: v for d in serialized_invoice for k, v in d.items()}["fields"]
        invoice_fields["date"] = parse(invoice_fields["date"]).strftime('%b. %d, %Y, %-I:%M %-p')
        invoice_fields["line_items"] = []
        for invoice_line_item in invoice.invoice_line_items.all():
            serialized_invoice_line_item = json.loads(serializers.serialize('json', [invoice_line_item]))
            serialized_invoice_line_item = {k: v for d in serialized_invoice_line_item for k, v in d.items()}
            invoice_fields["line_items"].append(serialized_invoice_line_item["fields"])
        return JsonResponse(invoice_fields)
