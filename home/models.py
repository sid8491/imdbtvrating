from django.db import models
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from django import forms


class HireMe(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=30, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    submit_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.email)


class Suggestion(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    suggestion = models.TextField(null=True, blank=True)
    submit_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.email)


class Projects(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField(null=True, blank=True)
    code = HTMLField(null=True, blank=True)
    coded_on = models.DateField(null=True, blank=True)
    new_code = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    def __str__(self):
        return str(self.name)

