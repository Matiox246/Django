# Generated by Django 5.1.2 on 2024-11-22 09:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_is_admin_user_is_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='premum_user',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Is Premum Until'),
        ),
    ]