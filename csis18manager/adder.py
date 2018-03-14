import smtplib
import csv

from delegate.models import Delegate
from track.models import Attendence,Track_Model , Track
from django.utils import timezone



Delegate.objects.all().delete()
Attendence.objects.all().delete()
Track_Model.objects.all().delete()
Track.objects.all().delete()

with open('del.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    temp = 0
    for row in spamreader:
        print(temp)
        temp+=1
        findel = Delegate(Csisid = row[2] , Fname = row[0] , Lname = row[1] , Registertime = timezone.now())
        tracks = ["General" , row[4] , row[5]]
        track_objs = []
        for i in tracks:
            if(len(Track_Model.objects.all().filter(TrackName = i) ) == 1):
                track_md = Track_Model.objects.get(TrackName = i)
            else:
                track_md = Track_Model(TrackName = i)
                track_md.save()
            at_obj = Attendence(last_checkin = timezone.now())
            at_obj.save()
            tr_obj = Track(Attendence = at_obj , TrackName = track_md)
            tr_obj.save()
            track_objs.append(tr_obj)
        findel.save()
        for i in track_objs:
            findel.Tracks.add(i)
        findel.save()
             
