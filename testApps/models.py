from django.db import models
from accounts.models import userProfile

class testApp(models.Model):
    applicationID = models.CharField(primary_key=True)
    applicationName = models.CharField(null=False)
    applicationDescription = models.CharField(max_length = 1000)
    applicationDownloads = models.IntegerField(default=0)
    uploaderID = models.OneToOneField(userProfile,on_delete=models.CASCADE)
    applicationVerdict = models.TextField(default='')
    applicationPartsToReview = models.TextField() #Takes each segment of the application the developer want reviewed separated by ','s
    
    def applicationQuestions(self):
        applicationParts = str(self.applicationPartsToReview).split(',')
        return applicationParts
    
    def getDetailsVisibleToStandardUSer(self):
        return self.applicationName,self.applicationDescription,self.applicationDownloads
    def getDetailsVisibleToDevelopers(self):
        return self.applicationID,self.applicationDownloads,self.applicationVerdict
    