from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from testApps.models import testApp
import django.utils.timezone

class userProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    userTags = models.CharField(max_length=1500,null=True,blank=True)
    applicationID = models.ForeignKey(testApp, on_delete=models.CASCADE)
    deviceDetails = models.TextField(max_length=50000)   
    appUsedFirstOn = models.DateField(default = django.utils.timezone.now)
    applicationFinalReview = models.TextField(max_length = 2500, blank = True, null=True,default='')    
    @receiver(post_save,sender=User)
    def create_user_profile(self,sender,instance,created,**kwargs):
        if created:
            self.objects.create(user = instance)
        
    @receiver(post_save,sender=User)
    def save_user_profile(self,sender,instance,**kwargs):
        instance.profile.save()

    def getApplicatonID(self):
        return self.applicationID

    def useStreak(self):
        return datetime.date.today() - self.appUsedFirstOn
    
    def getReview(self,appReview):
        self.applicationReview = appReview

