# Generated by Django 5.1.2 on 2024-11-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixed_cost', '0006_alter_fixedcost_custom_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedcost',
            name='deadline',
            field=models.CharField(choices=[('permanantly', 'permanantly'), ('custom', 'custom')], default='permanantly', max_length=50, verbose_name='deadline'),
        ),
        migrations.AlterField(
            model_name='fixedcost',
            name='schedule',
            field=models.CharField(choices=[('yearly', 'yearly'), ('monthly', 'monthly'), ('weekly', 'weekly'), ('daily', 'daily'), ('custom', 'custom')], default='monthly', max_length=50, verbose_name='schedule'),
        ),
    ]