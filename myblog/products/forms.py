from django import forms
from .models import *


class imageForm(forms.ModelForm):
    class Meta:
        model=images
        fields="__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'services': forms.Select(attrs={'class': 'form-control','placeholder':'services'})
        }




class visitorForm(forms.ModelForm):
    
    class Meta:
        model=visitor
        fields=['name','slug','gmail','subject','content',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Input Firstname'}),
            'gmail': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Somebody@gmail.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control','placeholder':'Subject'}),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder':'Content'}),
            'slug': forms.TextInput(attrs={'class': 'form-control','placeholder':'Input Surname'})
        }

