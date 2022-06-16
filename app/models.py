from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    hoodname = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    occupants = models.IntegerField()
    admin = models.ForeignKey()