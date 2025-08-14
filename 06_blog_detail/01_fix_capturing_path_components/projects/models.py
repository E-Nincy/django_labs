from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    technology = models.CharField(max_length=20)
