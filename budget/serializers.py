from rest_framework import serializers
from .models import Budget, Income, Expense, Category


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('id', 'name', 'description',)
