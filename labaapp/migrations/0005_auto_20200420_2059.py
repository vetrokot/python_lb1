# Generated by Django 3.0.5 on 2020-04-20 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labaapp', '0004_auto_20200420_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 20, 59, 8, 557720)),
        ),
    ]