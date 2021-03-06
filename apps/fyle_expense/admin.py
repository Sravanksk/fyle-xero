from django.contrib import admin

from apps.fyle_expense.models import Expense, ExpenseGroup


class ExpenseAdmin(admin.ModelAdmin):
    """
    Admin options for Expense model
    """
    list_display = ('expense_id', 'expense_number', 'employee_email',
                    'purpose', 'amount', 'created_at', 'updated_at')
    list_filter = ['expense_id', 'expense_number', 'employee_email',
                   'report_id', 'created_at', 'updated_at']


class ExpenseGroupAdmin(admin.ModelAdmin):
    """
    Admin options for ExpenseGroup model
    """
    list_display = ('id', 'status', 'created_at', 'updated_at')
    list_filter = ['status', 'created_at', 'updated_at']


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseGroup, ExpenseGroupAdmin)
