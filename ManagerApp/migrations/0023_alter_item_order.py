# Generated by Django 4.1.5 on 2023-02-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0022_rename_order_id_item_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
