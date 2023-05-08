# Generated by Django 3.2.3 on 2021-07-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=80)),
                ('category', models.CharField(choices=[('POLITICS', 'POLITICS'), ('SPORT', 'SPORT'), ('EDUCATION', 'EDUCATION'), ('SCIENCE&TECH', 'SCIENCE&TECH'), ('ENTERTAINMENT', 'ENTERTAINMENT'), ('GIST ROOM', 'GIST ROOM')], max_length=120)),
                ('images', models.ImageField(default='select image here', upload_to='product_images', verbose_name='upload image here')),
                ('content', models.TextField(max_length=120)),
            ],
        ),
    ]
