# Generated by Django 3.2.8 on 2021-10-12 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveSmallIntegerField(default=datetime.date.today, verbose_name='Год издания'),
        ),
    ]
