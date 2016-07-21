from django.db import models
from ckeditor.fields import RichTextField


class HireMe(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    number = models.CharField(max_length=30)
    comments = models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.email)


class Suggestion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    suggestion = models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.email)


class Projects(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()
    code = RichTextField()
    coded_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Project Entry"
        verbose_name_plural = "Project Entries"
        ordering = ['-coded_on']

