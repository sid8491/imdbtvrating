from django.db import models


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


