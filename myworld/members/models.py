import email
from operator import mod
from pickle import TRUE
from django.db import models

class Students(models.Model):
  name = models.CharField(max_length=255)
  ID =  models.IntegerField(primary_key=True,unique=True)
  birth=models.DateField()
  gpa= models.DecimalField(max_digits=3,decimal_places=2)
  male=models.BooleanField()
  level=models.IntegerField()
  active=models.BooleanField()
  dep=models.CharField(max_length=255)
  mail=models.CharField(max_length=255)
  phone=models.CharField(max_length=255)

class Employees(models.Model):
  mail=models.CharField(max_length=255,primary_key=True,unique=TRUE)
  password=models.CharField(max_length=255)