from django.db import models
from track.models import Track
# Create your models here.
class Delegate(models.Model):
    Csisid = models.IntegerField()
    Fname = models.CharField(max_length = 500)
    Lname = models.CharField(max_length = 500)
    Tracks = models.ManyToManyField(Track, blank=True)
    Registered = models.IntegerField(default = 0)
    Registertime = models.DateTimeField()