# Generated by Django 4.2.2 on 2023-06-25 20:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_courier_phone_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe tener el siguiente formato: '+código de país-número de área-número de teléfono'.", regex='^\\+53\\d{1}\\d{7}$')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe tener el siguiente formato: '+código de país-número de área-número de teléfono'.", regex='^\\+53\\d{1}\\d{7}$')]),
        ),
    ]
