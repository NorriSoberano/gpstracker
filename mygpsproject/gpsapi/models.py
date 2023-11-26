from django.db import models

class GPSData(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    velocity = models.FloatField()
    satellites = models.IntegerField()
    bearing = models.CharField(max_length=20)
