# Generated by Django 4.0.6 on 2023-07-13 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_delete_roomsmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='unit_of_measurement',
        ),
    ]
