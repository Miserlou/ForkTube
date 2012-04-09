from django.db import models
from django import forms 
from django.forms import ModelForm
from captcha.fields import CaptchaField

class ForkItem(models.Model):
    user = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=100, blank=False)
    hashish = models.CharField(max_length=100, blank=False)
    uploaded = models.BooleanField(default=False)
    downloaded = models.BooleanField(default=False)

class ForkItemForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ForkItem
        exclude = ('hashish', 'uploaded', 'downloaded')
