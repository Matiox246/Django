# Generated by Django 5.1.2 on 2024-11-22 09:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_premum_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='premum_user',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Is Premum Until'),
        ),
    ]