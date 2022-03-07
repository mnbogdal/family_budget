from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BudgetSerializer
from .models import Budget
from .filtersets import BudgetFilterSet


class BudgetView(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    filterset_class = BudgetFilterSet
    queryset = Budget.objects.all()
