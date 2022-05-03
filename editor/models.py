from django.db import models

class UserFiles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200)
    js = models.TextField(blank=True)
    html = models.TextField(blank=True)
    css = models.TextField(blank=True)
