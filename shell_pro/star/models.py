from django.db import models

# Create your models here.

class Mastaru(models.Model):
    name = models.CharField(max_length=15)