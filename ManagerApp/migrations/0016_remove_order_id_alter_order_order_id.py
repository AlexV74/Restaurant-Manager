# Generated by Django 4.1.5 on 2023-02-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0015_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
