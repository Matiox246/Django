# Generated by Django 5.1.2 on 2024-11-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10, verbose_name='first name')),
                ('lname', models.CharField(max_length=50, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('message', models.CharField(max_length=200, verbose_name='message')),
                ('time', models.DateField(auto_now_add=True, verbose_name='time')),
            ],
        ),
    ]
