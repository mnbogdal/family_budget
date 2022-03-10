from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model

from .models import Budget, Income, Expense, Category


User = get_user_model()


class BudgetFilterSet(filters.FilterSet):
    strict = True
    assigned_budgets = filters.NumberFilter(method='get_assigned_budgets')

    class Meta:
        model = Budget
        fields = [
            'name',
            'description',
            'owner',
            'assigned_budgets'
        ]

    def get_assigned_budgets(self, queryset, name, value):
        return queryset.filter(users__in=[value])


class ExpenseFilterSet(filters.FilterSet):
    strict = True

    class Meta:
        model = Expense
        fields = [
            'name',
            'description',
            'value',
            'category',
            'budget'
        ]


class IncomeFilterSet(filters.FilterSet):
    strict = True

    class Meta:
        model = Income
        fields = [
            'name',
            'description',
            'value',
            'category',
            'budget'
        ]


class CategoryFilterSet(filters.FilterSet):
    strict = True

    class Meta:
        model = Category
        fields = [
            'name',
        ]
