# Generated by Django 3.2.3 on 2023-02-28 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20230228_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
