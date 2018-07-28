from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from testApps.models import testapps
import datetime
class testUser(models.Model):
    userTags = models.CharField(max_length=1500,null=True,blank=True)
    applicationID = models.ForeignKeyField(testapps, on_delete=models.CASCADE)
#   deviceDetails = models.CharField()   Replace this with appropriate dataType most possibly a CharField or SlugField
    appUsedFirstOn = models.DateTimeField(default = datetime.datetime.today())
    
    def newTester(self,appID,appEnrolled):
        self.applicationID = appID
        self.appUsedFirstOn = appEnrolled
        self.save()

    def getApplicatonID(self):
        return self.applicationID

    def useStreak(self):
        return datetime.datetime.today() - self.appUsedFirstOn
    
    