from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from testApps.models import testapps
import datetime
class testUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    userTags = models.CharField(max_length=1500,null=True,blank=True)
    applicationID = models.ForeignKey(testapps, on_delete=models.CASCADE)
#   deviceDetails = models.CharField()   Replace this with appropriate dataType most possibly a CharField or SlugField
    appUsedFirstOn = models.DateField(default = datetime.datetime.today())
    applicationReview = models.CharField(max_length = 2500, blank = True, null=True,default='')    
    
    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            testUser.objects,create(user = instance)
        
    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

    def getApplicatonID(self):
        return self.applicationID

    def useStreak(self):
        return datetime.date.today() - self.appUsedFirstOn
    
    def getReview(self,appReview):
        self.applicationReview = appReview

class Developer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    appsDeveloped = models.ForeignKey(testapps,on_delete=models.CASCADE)
        @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            testUser.objects,create(user = instance)
        
    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()