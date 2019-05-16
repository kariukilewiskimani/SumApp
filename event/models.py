from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=70)
    event_host = models.CharField(max_length=45)
    event_cover = models.FileField()

class Detail(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.TextField()
    place = models.CharField(max_length=80)
    time = models.DateTimeField()
