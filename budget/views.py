from rest_framework import viewsets
from .serializers import BudgetSerializer, ExpenseSerializer, \
    IncomeSerializer, CategorySerializer
from .models import Budget, Expense, Income, Category
from .filtersets import BudgetFilterSet, IncomeFilterSet, \
    ExpenseFilterSet, CategoryFilterSet


class BudgetView(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    filterset_class = BudgetFilterSet
    queryset = Budget.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    filterset_class = ExpenseFilterSet
    queryset = Expense.objects.all()


class IncomeView(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    filterset_class = IncomeFilterSet
    queryset = Income.objects.all()


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    filterset_class = CategoryFilterSet
    queryset = Category.objects.all()
