# Generated by Django 3.2.5 on 2021-07-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageapp', '0002_auto_20210422_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addevent',
            name='Fund',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='addevent',
            name='Venue',
            field=models.CharField(max_length=20),
        ),
    ]
