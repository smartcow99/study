from django.db import models

# Create your models here.
class Ieee(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  answer = models.IntegerField()