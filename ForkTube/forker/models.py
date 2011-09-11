from django.db import models
from django import forms 
from django.forms import ModelForm

class ForkItem(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    hashish = models.CharField(max_length=100)
    uploaded = models.BooleanField(default=False)
    downloaded = models.BooleanField(default=False)

class ForkItemForm(ModelForm):
    class Meta:
        model = ForkItem 
