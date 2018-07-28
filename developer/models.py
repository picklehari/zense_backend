from django.db import models
from django.contrib.auth.models import User

class developer(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        devID = models.IntegerField(primary_key=True)
