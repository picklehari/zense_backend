from django.db import models
from accounts.models import userProfile

class testApp(models.Model):
    applicationID = models.CharField(pk=True)
