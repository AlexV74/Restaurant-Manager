# Generated by Django 4.1.5 on 2023-03-21 18:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0028_order_table_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_number', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(40)])),
                ('need_help', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='table_number',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
