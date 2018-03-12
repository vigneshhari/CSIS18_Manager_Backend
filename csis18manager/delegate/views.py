from django.shortcuts import render
from django.http import JsonResponse

from .models import Delegate
# Create your views here.

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
            data.append({"name" : i.TrackName , "hour" : i.Attendence.Total_Time})
    return JsonResponse( {"name" : temp.Fname + " " + temp.Lname , "track" : data})

def registermain(request):
    pass

def registertrack(request):
    pass

def deregistertrack(request):
    pass

def listattendtrack(request):
    pass

def listmissingtrack(request):
    pass
