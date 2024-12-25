# Generated by Django 5.1.2 on 2024-12-13 20:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0012_expense_goal_user_income_goal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]