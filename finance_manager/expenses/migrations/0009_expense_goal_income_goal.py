# Generated by Django 5.1.2 on 2024-12-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_alter_expense_user_alter_income_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='goal',
            field=models.IntegerField(null=True, verbose_name='goal'),
        ),
        migrations.AddField(
            model_name='income',
            name='goal',
            field=models.IntegerField(null=True, verbose_name='goal'),
        ),
    ]