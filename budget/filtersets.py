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
