# Generated by Django 3.2.12 on 2022-03-08 00:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20220308_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 3, 8, 0, 30, 29, 403959, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='income',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 3, 8, 0, 31, 39, 19767, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
