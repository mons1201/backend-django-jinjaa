from datetime import datetime
from http import client
from django.http import HttpResponse
from django.shortcuts import redirect, render
from mongoengine import *
from certifi import *
from . import documents

myCert=where()
client=connect(host="mongodb+srv://mohan:mohan@cluster0.traigro.mongodb.net/?retryWrites=true&w=majority",db="sympoo",username="mohan",password="mohan",tlsCAFile=myCert)


# Create your views here.
def makeDelete(req,unique):
    receive=documents.Event.objects(eveId=unique).first()
    receive.delete()
    return redirect('/buddy/')

def makeEdit(req,num):
    if req.method=="POST":
        d=req.POST['eveid']
        nm=req.POST['evename']
        dt=req.POST['evedate']
        dp=req.POST['evedept']
        documents.Event.objects(eveId=d).update_one(set__eveName=nm,set__eveDate=dt,set__eveDepartment=dp)
        return redirect('/buddy/')
    else:
        receive=documents.Event.objects(eveId=num).first()
        return render(req,'edit.html',{"record":receive})

def makeRead(req,seriel):
    receive=documents.Event.objects(eveId=seriel).first()
    return render(req,'one.html',{"data":receive})

def makeCreate(req):
    if req.method=="POST":
        #print("POST accepted")
        nm=req.POST['evename']
        dt=req.POST['evedate']
        dp=req.POST['evedept']
        #print(nm,dt,dp)
        eve=documents.Event()
        eve.initiate(nm,datetime.fromisoformat(dt),dp)
        eve.save()
        return render(req,'schedule.html',{"info":nm+ "has scheduled" })
    else:
        return render(req,'schedule.html')
        
    '''eve=documents.Event()
    eve.initiate("Sparkers17",datetime.fromisoformat("2022-10-10"),"EEE")
    eve.save()
    return HttpResponse('event has added')
'''
def makeList(req):
    mine=documents.Event.objects.all()
    # for x in mine:print(x)
    # return HttpResponse("Event has listed")
    return render(req,'viewing.html',{"everything":mine})
def makePage(req):
    return render(req,'begin.html')
