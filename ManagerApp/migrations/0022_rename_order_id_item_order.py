# Generated by Django 4.1.5 on 2023-02-23 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0021_alter_item_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='order_id',
            new_name='order',
        ),
    ]
