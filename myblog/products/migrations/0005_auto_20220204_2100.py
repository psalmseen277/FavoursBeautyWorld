# Generated by Django 3.2.3 on 2022-02-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_images_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='facial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('service', models.CharField(choices=[('MASSAGE', 'MASSAGE'), ('FACIAL', 'FACIAL')], max_length=20, null=True, verbose_name='choose the service')),
            ],
        ),
        migrations.CreateModel(
            name='massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('service', models.CharField(choices=[('MASSAGE', 'MASSAGE'), ('FACIAL', 'FACIAL')], max_length=20, null=True, verbose_name='choose the service')),
            ],
        ),
        migrations.AddField(
            model_name='images',
            name='service',
            field=models.CharField(choices=[('MASSAGE', 'MASSAGE'), ('FACIAL', 'FACIAL')], max_length=20, null=True, verbose_name='choose the service'),
        ),
    ]
