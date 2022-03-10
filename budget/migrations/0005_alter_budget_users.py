# Generated by Django 3.2.12 on 2022-03-08 00:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0004_auto_20220308_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='users',
            field=models.ManyToManyField(related_name='budgets', to=settings.AUTH_USER_MODEL, verbose_name='Users'),
        ),
    ]
