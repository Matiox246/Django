# Generated by Django 5.1.2 on 2024-11-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixed_cost', '0001_initial'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='fixedcost',
        #     name='schedule_custom',
        # ),
        # migrations.AddField(
        #     model_name='fixedcost',
        #     name='schedule_custom',
        #     field=models.CharField(max_length=100, null=True, verbose_name='schedule_custom'),
        # ),
        migrations.AlterField(
            model_name='fixedcost',
            name='amount',
            field=models.IntegerField(verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='fixedcost',
            name='deadline_custom',
            field=models.DateField(verbose_name='deadline_custom'),
        ),
        migrations.AlterField(
            model_name='fixedcost',
            name='schedule',
            field=models.CharField(choices=[('Y', 'yearly'), ('M', 'monthly'), ('W', 'weekly'), ('D', 'daily'), ('C', 'custom')], default='M', max_length=2, verbose_name='schedule'),
        ),
    ]
