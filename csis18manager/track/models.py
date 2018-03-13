from django.db import models

# Create your models here.
class Track(models.Model):
    TrackName = models.ForeignKey('Track_Model' , blank=True , on_delete=models.CASCADE)
    Attendence = models.ForeignKey('Attendence' , blank=True , on_delete=models.CASCADE)

class Track_Model(models.Model):
    TrackName = models.CharField(max_length = 500) 

class Attendence(models.Model):
    Attending = models.IntegerField(default=0)
    Total_Time = models.IntegerField(default=0)
    last_checkin = models.DateTimeField()
