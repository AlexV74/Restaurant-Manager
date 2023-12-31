# Generated by Django 4.1.5 on 2023-02-23 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0019_item_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='order_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_items', to='ManagerApp.order'),
        ),
    ]
