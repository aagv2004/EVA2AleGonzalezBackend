# Generated by Django 3.2 on 2024-10-28 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(20)])),
                ('apellido', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(20)])),
                ('correo', models.CharField(max_length=50, validators=[django.core.validators.EmailValidator('El correo debe llevar @')])),
            ],
        ),
    ]
