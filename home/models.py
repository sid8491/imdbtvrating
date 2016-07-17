from django.db import models
from django_markdown.models import MarkdownField
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
    code = MarkdownField()
    coded_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Project Entry"
        verbose_name_plural = "Project Entries"
        ordering = ['-coded_on']

