# Generated by Django 4.1.5 on 2023-02-20 18:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0012_menucategory_alter_menuitems_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menucategory',
            options={'verbose_name_plural': 'Menu Categories'},
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='calories',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='ingredients',
            field=models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(limit_value=200, message='Ingredients list is too long'), django.core.validators.RegexValidator(message='Invalid characters in ingredients list', regex='^[a-zA-Z,.\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
