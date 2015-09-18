from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Regular(models.Model):
	user = models.OneToOneField(User)
	isAdmin = models.BooleanField()

class Location(models.Model):
	name = models.CharField(max_length=850)
	description = models.TextField(max_length = 800)
	locationLink = models.CharField(max_length = 800)
	owner = models.ForeignKey(User_Regular)

class Box(models.Model):
	Box_ID = models.IntegerField(primary_key=True)
	Capacity = models.IntegerField()
	Location = models.ForeignKey(Location)

class Log(models.Model):
	NumberOfCaps =  models.IntegerField()
	Timestamp = models.TimeField()
	Box = models.ForeignKey(Box)

