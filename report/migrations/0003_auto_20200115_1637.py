# Generated by Django 2.2 on 2020-01-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20200115_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='average_speed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
