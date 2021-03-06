# Create your views here.
from django import forms
from django.utils import timezone 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import Location, Box, Log, User_Regular
from datetime import datetime, timedelta 
import pytz


GOAL = 1000

def makeLog(number, full, box_ID):
    box = Box.objects.get(id = box_ID)

    log = Log(Box = box)
    log.NumberOfCaps = number
    log.isFull = full
    log.save()


def adduser(request):
    request.session.set_expiry(0)

    username = request.POST['username']
    password = request.POST['pass']
    email = request.POST['email']

    user = User.objects.create_user(username, email, password)
    newUser = User_Regular()
    newUser.user = user
    newUser.isAdmin = False
    newUser.save()

    return redirect('admin')

def getCapSum():
    capSum = 0
    logs = Log.objects.all()
    for log in logs:
        capSum += log.NumberOfCaps

    return capSum

def percentCompleted():
    capSumGoal = float(getCapSum()%GOAL)
    percent = (capSumGoal/GOAL)*100
    return percent

def daysLeft():
    capSum = 0
    date = datetime.now(pytz.utc)
    fiveDaysAgo = date+timedelta(days=-5)
    logs = Log.objects.all()
    
    for log in logs:
        if log.Timestamp > fiveDaysAgo:
            capSum+= log.NumberOfCaps
    
    mean = float(capSum)/5
    if mean == 0:
        return 30
        
    daysLeft = (GOAL-(getCapSum()%GOAL))/mean
    
    return round(daysLeft, 2)

def home(request):
    #makeLog()
    capSum = getCapSum()

    ctx = {'capSum':capSum, 'percent': percentCompleted(),'daysLeft':daysLeft()}
    return render(request, "home.html", ctx)

def admin(request):
    locations = Location.objects.all()
    boxes = Box.objects.all()
    users = User_Regular.objects.all()

    ctx = {'locations':locations, 'boxes':boxes, 'users':users}
    return render(request, "admin.html", ctx)

def addlocation(request):
    request.session.set_expiry(0)
    
    location = Location()
    location.name = request.POST['name']
    location.locationImg = request.POST['locationImg']
    location.description = request.POST['description']
    location.locationLink = request.POST['locationLink']
    location.longitude = request.POST['longitude']
    location.latitude = request.POST['latitude']
    user_id = request.POST['sel1']
    userUser = User.objects.get(id = user_id)
    user = User_Regular.objects.get(user = userUser)
    location.owner = user
    location.save() 

    return redirect('admin')

def addbox(request):
    request.session.set_expiry(0)
    box = Box()
    location_id = request.POST['sel2']
    box.Location = Location.objects.get(id = location_id)
    box.save()

    return redirect('admin')

@csrf_exempt
def api(request):
    number = request.POST['NumberOfCaps']
    full = request.POST['isFull']
    box_ID = request.POST['Box']
    makeLog(number, full, box_ID)
    return HttpResponse(status = 200)

def locations(request):
    
    locations = Location.objects.all()

    ctx = {'locations': locations}

    return render(request, "locations.html", ctx)

def location(request):
    location_id = request.GET.get('id')
    location = Location.objects.get(id = location_id)
    ctx = {'location': location} 
    return render(request, "location.html",ctx)

