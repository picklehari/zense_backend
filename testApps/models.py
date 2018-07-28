from django.db import models
from developer.models import developer

class testApp(models.Model):
    applicationID = models.CharField(max_length=100,primary_key=True)
    applicationName = models.CharField(max_length=100,null=False)
    applicationDescription = models.CharField(max_length = 1000)
    applicationDownloads = models.IntegerField(default=0)
    uploaderID = models.ForeignKey(developer,on_delete=models.CASCADE)
    applicationVerdict = models.TextField(default='')
    applicationPartsToReview = models.TextField() #Takes each segment of the application the developer want reviewed separated by ','s
    
    def applicationQuestions(self):  #Splits each applicationParts.Everything to be be converted as questions
        applicationParts = str(self.applicationPartsToReview).split(',')
        return applicationParts
    
    def getDetailsVisibleToStandardUSer(self): #Returns tuple of details that can be viewed by the standard Test User
        return self.applicationName,self.applicationDescription,self.applicationDownloads

    def getDetailsVisibleToDevelopers(self): #Returns tuple of details that is visible to only the developer peeps
        return self.applicationID,self.applicationDownloads,self.applicationVerdict
