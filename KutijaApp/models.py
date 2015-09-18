from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Regular(models.Model):
	user = models.OneToOneField(User)
	isAdmin = models.BooleanField()

class Location(models.Model):
	name = models.CharField(max_length=850)            # Location name - example "Faculty of Organizational Sciences" 
	locationImg = models.CharField(max_length =850)    # Location image
	description = models.TextField(max_length = 800)   # Location description 
	locationLink = models.CharField(max_length = 800)  # Link to otganization website
	longitude = models.CharField(max_length =800)	   # Longitude for Google Maps
	latitude = models.CharField(max_length =800)	   # Latitude for Google Maps
	owner = models.ForeignKey(User_Regular) 

class Box(models.Model):
	Box_ID = models.IntegerField(primary_key=True)    
	
	Location = models.ForeignKey(Location)

class Log(models.Model):
	NumberOfCaps =  models.IntegerField()
	Timestamp = models.TimeField()
	isFull = models.BooleanField()
	Box = models.ForeignKey(Box)

