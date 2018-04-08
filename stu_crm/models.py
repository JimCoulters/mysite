from django.db import models

# Create your models here.
from django.db import models
import datetime

from django.utils import timezone

class Station(models.Model):
    protostatid = models.AutoField(primary_key=True)
    projectname = models.CharField(max_length=250)
    stationname = models.CharField(max_length=250)

class BuStation(models.Model):
    proid =	 models.AutoField(primary_key=True)
    propertyunit = models.CharField(max_length=250)
    projecttime = models.IntegerField()
    projectname = models.CharField(max_length=250)
    projectfunds = models.FloatField()
    settlement = models.CharField(max_length=250)
    settlementfunds = models.FloatField()
    surplusfunds = models.FloatField()
    transferfunds = models.FloatField()
    depreciation = models.FloatField()
    netassets = models.FloatField()
    renovationproject = models.FloatField()
    renovationtime = models.FloatField()
    renovationfunds = models.FloatField()
