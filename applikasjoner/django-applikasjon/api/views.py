from django.http import HttpResponse
from django.shortcuts import render
import time
from datetime import datetime as dt
  
from .models import AppDB

# Create your views here.
def add(request):
    try:
        intervall = int(request.GET.get("int"))
    except:
        intervall = 0
    siste = AppDB.objects.latest('id')
    siste_tid = siste.tidspunkt

    nå = dt.now()
    milli = round(time.time() * 1000)

    tid_siden_siste = milli - int(siste_tid)
    

    ny = AppDB(tidspunkt=milli, tid=nå, intervall=intervall)#tid_siden_siste=tid_siden_siste
    ny.save()

    return HttpResponse("Suksess")