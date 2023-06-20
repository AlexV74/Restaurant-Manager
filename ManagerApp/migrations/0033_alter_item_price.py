# Generated by Django 4.1.5 on 2023-03-23 21:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0032_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]