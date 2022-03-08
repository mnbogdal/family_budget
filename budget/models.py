from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='budgets',)

    def _str_(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120)

    def _str_(self):
        return f"{self.name}"


class Expense(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    value = models.IntegerField(default=0)
    budget = models.ForeignKey(Budget,
                               related_name='expenses',
                               null=True, blank=True,
                               verbose_name='Expense budget',
                               on_delete=models.SET_NULL)
    category = models.ForeignKey(Category,
                                 related_name='expenses',
                                 null=True, blank=True,
                                 verbose_name='Expense category',
                                 on_delete=models.SET_NULL)

    def _str_(self):
        return f"{self.name} {self.value}"


class Income(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    value = models.IntegerField(default=0)
    budget = models.ForeignKey(Budget,
                                 related_name='incomes',
                                 null=True, blank=True,
                                 verbose_name='Income budget',
                                 on_delete=models.SET_NULL)
    category = models.ForeignKey(Category,
                                 related_name='incomes',
                                 null=True, blank=True,
                                 verbose_name='Income category',
                                 on_delete=models.SET_NULL)

    def _str_(self):
        return f"{self.name} {self.value}"



