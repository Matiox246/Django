# Generated by Django 5.1.2 on 2024-11-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixed_cost', '0005_alter_fixedcost_custom_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedcost',
            name='custom_deadline',
            field=models.DateField(blank=True, null=True, verbose_name='deadline_custom'),
        ),
        # migrations.AlterField(
        #     model_name='fixedcost',
        #     name='schedule_custom',
        #     field=models.DateField(blank=True, null=True, verbose_name='chedule_custom'),
        # ),
    ]
