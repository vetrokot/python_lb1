# Generated by Django 3.0.5 on 2020-04-26 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labaapp', '0022_auto_20200426_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 19, 37, 6, 265990)),
        ),
    ]