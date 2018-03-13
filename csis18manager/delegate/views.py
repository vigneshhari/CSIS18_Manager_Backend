from django.shortcuts import render
from django.http import JsonResponse
import datetime
from .models import Delegate
from track.models import Track , Attendence , Track_Model
from django.utils import timezone

def minutes(td):
    return (td.seconds//60)%60

def info(request):
    if( 'csisid' not in request.GET.keys()):
        return JsonResponse({"statuscode" : "404"})
    datadel = Delegate.objects.all().filter(Csisid = request.GET.get('csisid'))
    if(len(datadel) == 0):
        return JsonResponse({'statuscode' : "303"})
    for i in datadel:temp = i;break
    data = []
    for i in Delegate.objects.get(Csisid = request.GET.get('csisid')).Tracks.all():
        if(i.Attendence.Total_Time != 0):
            data.append({"name" : i.TrackName.TrackName , "hour" : str(i.Attendence.Total_Time)})
    return JsonResponse( { 'statuscode' : "100", "name" : temp.Fname + " " + temp.Lname , "track" : data})

def registermain(request):
    if( 'csisid' not in request.GET.keys() ):
        return JsonResponse({"statuscode" : "404"})
    datadel = Delegate.objects.all().filter(Csisid = request.GET.get('csisid') , Registered = 0)
    if(len(datadel) == 0):
        return JsonResponse({'statuscode' : "303"})
    Delegate.objects.all().filter(Csisid = request.GET.get('csisid')).update(Registered = 1 , Registertime = timezone.now())
    return JsonResponse({'statuscode' : '100'})


def registertrack(request):
    if( 'csisid' not in request.GET.keys() or 'track' not in request.GET.keys() ):
        return JsonResponse({"statuscode" : "404"})
    datadel = Delegate.objects.all().filter(Csisid = request.GET.get('csisid'))
    if(len(datadel) == 0):
        return JsonResponse({'statuscode' : "303"})
    for i in Delegate.objects.get(Csisid = request.GET.get('csisid')).Tracks.all():
        if(i.TrackName.TrackName == request.GET.get('track') ):
            Trackobj = Track_Model.objects.get(TrackName = request.GET.get('track'))
            temp = Delegate.objects.get(Csisid = request.GET.get('csisid')).Tracks.get( TrackName  = Trackobj ).Attendence
            temp.Attending = 1
            temp.last_checkin = timezone.now()
            temp.save()
            return JsonResponse({"statuscode" : 100})

    return JsonResponse({"statuscode" : '500'})

def deregistertrack(request):
    if( 'csisid' not in request.GET.keys() or 'track' not in request.GET.keys() ):
        return JsonResponse({"statuscode" : "404"})
    datadel = Delegate.objects.all().filter(Csisid = request.GET.get('csisid'))
    if(len(datadel) == 0):
        return JsonResponse({'statuscode' : "303"})
    for i in Delegate.objects.get(Csisid = request.GET.get('csisid')).Tracks.all():
        if(i.TrackName.TrackName == request.GET.get('track') ):
            Trackobj = Track_Model.objects.get(TrackName = request.GET.get('track'))
            temp = Delegate.objects.get(Csisid = request.GET.get('csisid')).Tracks.get( TrackName  = Trackobj ).Attendence
            temp.Attending = 0
            FMT = '%H:%M:%S'
            temp.Total_Time = temp.Total_Time + minutes(  timezone.now() -  temp.last_checkin)
            temp.save()
            return JsonResponse({"statuscode" : 100})
            
    return JsonResponse({"statuscode" : '500'})

def listattendtrack(request):
    if( 'csisid' not in request.GET.keys() or 'track' not in request.GET.keys() ):
        return JsonResponse({"statuscode" : "404"})
    datadel = Delegate.objects.all().filter(Csisid = request.GET.get('csisid'))
    if(len(datadel) == 0):
        return JsonResponse({'statuscode' : "303"})
    Trackobj = Track_Model.objects.get(TrackName = request.GET.get('track'))
    delegates = Delegate.objects.all().filter(Tracks__TrackName = Trackobj , Tracks__Attendence__Attending = 1)
    data = []
    for i in delegates:
        data.append({"name" : i.Fname + " " + i.Lname})
    return JsonResponse({ "data" : data , "statuscode" : "100"} )


def listmissingtrack(request):
    if( 'csisid' not in request.GET.keys() or 'track' not in request.GET.keys() ):
        return JsonResponse({"statuscode" : "404"})
    datadel = Delegate.objects.all().filter(Csisid = request.GET.get('csisid'))
    if(len(datadel) == 0):
        return JsonResponse({'statuscode' : "303"})
    Trackobj = Track_Model.objects.get(TrackName = request.GET.get('track'))
    delegates = Delegate.objects.all().filter(Tracks__TrackName = Trackobj , Tracks__Attendence__Attending = 0)
    data = []
    for i in delegates:
        data.append({"name" : i.Fname + " " + i.Lname})
    return JsonResponse({ "data" : data , "statuscode" : "100"} )

def listtracks(request):
    data = []
    for i in Track_Model.objects.all():
        data.append({"name" : i.TrackName})
    return JsonResponse({'statuscode' : "100" , "data" : data})