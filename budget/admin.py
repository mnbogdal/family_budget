from django.contrib import admin
from django.contrib.auth.models import User

from .models import Category, Income, Expense, Budget


class UserInline(admin.StackedInline):
    model = User.budgets.through
    extra = 1
    # filter_horizontal = ('',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'value', 'category')


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'value', 'category')


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    inlines = (UserInline,)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Budget, BudgetAdmin)
