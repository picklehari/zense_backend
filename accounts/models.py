from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from testApps.models import testApp
import django.utils.timezone
import datetime

class userProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    userTags = models.CharField(max_length=1500,null=True,blank=True)
    applicationID = models.ForeignKey(testApp, on_delete=models.CASCADE)
    deviceDetails = models.TextField(max_length=50000)   
    appUsedFirstOn = models.DateField(default = django.utils.timezone.now)
    applicationFinalReview = models.TextField(max_length = 2500, blank = True, null=True,default='')    
