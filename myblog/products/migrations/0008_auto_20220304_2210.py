# Generated by Django 3.2.3 on 2022-03-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_images_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gmail', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=10, verbose_name='input inquries here')),
            ],
        ),
        migrations.AlterField(
            model_name='images',
            name='services',
            field=models.CharField(choices=[('skincare', 'skincare'), ('massage', 'massage'), ('facial', 'facial'), ('piercing', 'piercing'), ('hair treatment', 'hair treatment'), ('nail treatment', 'nail treatment')], max_length=120, verbose_name='Select Service'),
        ),
    ]
