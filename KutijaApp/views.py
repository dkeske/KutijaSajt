# Create your views here.
from django.shortcuts import render, redirect
from models import Location, Box, Log, User_Regular
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):


	return render(request, "home.html")