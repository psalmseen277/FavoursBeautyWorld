# Generated by Django 3.2.3 on 2023-02-28 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_visitor_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='visitor',
            new_name='visitors',
        ),
    ]
