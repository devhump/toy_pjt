from django.db import models

# Create your models here.
class WiseSaying(models.Model):
    contents = models.CharField(max_length=50)
    count = models.IntegerField()
