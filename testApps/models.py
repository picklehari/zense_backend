from django.db import models
from developer.models import developer

class testApp(models.Model):
    applicationID = models.CharField(max_length=100,primary_key=True)
    applicationName = models.CharField(max_length=100,null=False)
    applicationDescription = models.CharField(max_length = 1000)
    applicationDownloads = models.IntegerField(default=0)
    application = models.FileField(blank=True)
    uploaderID = models.ForeignKey(developer,on_delete=models.CASCADE)
    applicationVerdict = models.TextField(default='')
    applicationPartsToReview = models.TextField() #Takes each segment of the application the developer want reviewed separated by ','s
    