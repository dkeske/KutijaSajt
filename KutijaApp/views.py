# Create your views here.
from django.shortcuts import render, redirect
from models import Location, Box, Log, User_Regular
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta 
from django.utils import timezone 
import pytz

GOAL = 100

def makeLog():
	user = User.objects.create_user('john', 's@g.com', 'johnpass')
	newUser = User_Regular()
	newUser.user = user
	newUser.save()

	newLocation = Location()
	#userP = authenticate(username = 'john', password = 'johnpass')
	#newUser = User_Regular.objects.get(user = userP)
	newLocation.owner = newUser
	newLocation.save()

	
	newBox = Box(Location = newLocation)
	
	newBox.save()

	newLog = Log(NumberOfCaps = 10, isFull = False, Box = newBox)
	
	newLog.save()

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
	daysLeft = (GOAL-(getCapSum()%GOAL))/mean
	
	return daysLeft

def home(request):
	#makeLog()
	capSum = getCapSum()

	ctx = {'capSum':capSum, 'percent': percentCompleted(),'daysLeft':daysLeft()}
	return render(request, "home.html", ctx)

def admin(request):
	locations = Location.objects.all()
	boxes = Box.objects.all()

	ctx = {'locations':locations, 'boxes':boxes}
	return render(request, "admin.html", ctx)