from django.db import models
from datetime import *
from django import forms
from django.forms import widgets
from django.forms.widgets import TextInput,EmailInput

# Create your models here
SERVICE=[
        ('skincare','skincare'),
        ('massage','massage'),
        ('facial','facial'),
        ('piercing','piercing'),
        ('hair treatment','hair treatment'),
        ('nail treatment','nail treatment'),
]
class images(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(max_length=100,upload_to='images/')
    services = models.CharField("Select Service",choices=SERVICE,max_length=120)

class visitor(models.Model):
    slug = models.SlugField("Surname",default="")
    name = models.CharField("First name",max_length=100)
    gmail = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    time = models.DateTimeField(default=datetime.now)