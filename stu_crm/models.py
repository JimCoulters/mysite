from django.db import models

# Create your models here.
from django.db import models
import datetime

from django.utils import timezone

class customer(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    id1 = models.IntegerField()
    qq = models.IntegerField()
    name = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    cource = models.CharField(max_length=200)
    get_class_type_display = models.CharField(max_length=200)
    customer_note = models.CharField(max_length=200)
    get_status_display=models.CharField(max_length=200)
    consultant = models.CharField(max_length=200)
    date = models.DateTimeField('date publicshed')
