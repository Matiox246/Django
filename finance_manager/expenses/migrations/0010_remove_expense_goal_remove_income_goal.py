# Generated by Django 5.1.2 on 2024-12-08 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0009_expense_goal_income_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='income',
            name='goal',
        ),
    ]