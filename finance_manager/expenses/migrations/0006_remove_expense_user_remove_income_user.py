# Generated by Django 5.1.2 on 2024-11-16 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_expense_user_alter_income_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
        migrations.RemoveField(
            model_name='income',
            name='user',
        ),
    ]
