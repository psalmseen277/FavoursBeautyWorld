# Generated by Django 3.2.3 on 2023-02-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20230208_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='slug',
            field=models.SlugField(default='', verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='content',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='gmail',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='name',
            field=models.CharField(max_length=100, verbose_name='First name'),
        ),
    ]
