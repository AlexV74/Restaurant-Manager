# Generated by Django 4.1.5 on 2023-02-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0005_staff_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu/images/')),
                ('ingredients', models.TextField(blank=True)),
                ('calories', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
