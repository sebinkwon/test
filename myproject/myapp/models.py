from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    s_id = models.CharField(max_length=10)