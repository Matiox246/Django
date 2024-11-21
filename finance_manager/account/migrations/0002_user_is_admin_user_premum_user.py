# Generated by Django 5.1.2 on 2024-11-21 10:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Membership type'),
        ),
        migrations.AddField(
            model_name='user',
            name='premum_user',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Membership type'),
        ),
    ]