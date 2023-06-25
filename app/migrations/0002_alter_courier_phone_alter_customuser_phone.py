# Generated by Django 4.2.2 on 2023-06-25 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe tener el siguiente formato: '+código de país-número de área-número de teléfono'.", regex='^\\+\\d{1,3}-\\d{1,4}-\\d{1,4}$')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe tener el siguiente formato: '+código de país-número de área-número de teléfono'.", regex='^\\+\\d{1,3}-\\d{1,4}-\\d{1,4}$')]),
        ),
    ]
