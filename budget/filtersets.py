from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model

from .models import Budget, Income, Expense, Category


User = get_user_model()


class BudgetFilterSet(filters.FilterSet):
    strict = True

    class Meta:
        model = Budget
        fields = [
            'name',
            'description',
        ]


class ExpenseFilterSet(filters.FilterSet):
    strict = True

    class Meta:
        model = Expense
        fields = [
            'name',
            'description',
        ]


class IncomeFilterSet(filters.FilterSet):
    strict = True

    class Meta:
        model = Income
        fields = [
            'name',
            'description',
        ]


class CategoryFilterSet(filters.FilterSet):
    strict = True

    class Meta:
        model = Category
        fields = [
            'name',
        ]
