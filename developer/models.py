from django.db import models
from django.contrib.auth.models import User

class developer(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        devID = models.AutoField(primary_key=True)
