# Generated by Django 4.1.5 on 2023-02-08 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0003_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ready',
        ),
    ]
