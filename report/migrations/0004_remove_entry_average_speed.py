# Generated by Django 2.2 on 2020-01-18 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20200115_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='average_speed',
        ),
    ]
