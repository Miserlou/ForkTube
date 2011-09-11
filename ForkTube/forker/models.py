from django.db import models
from django import forms 
from django.forms import ModelForm

class ForkItem(models.Model):
    user = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    url = forms.CharField(max_length=100)

class ForkItemForm(ModelForm):
    class Meta:
        model = ForkItem 
