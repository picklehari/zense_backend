from django.contrib.auth.models import User
from rest_framework import serializers
from .models import userProfile
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email')
<<<<<<< HEAD

class profileSerializer(serializers.Serializer):
    class Meta:
        model = userProfile
        field= ('user','userTags','applicationID','deviceDetails','appUsedFirstOn','applicationFinalReview')
        
=======
def create(self,validated_data):
    return userProfile.objects.create(**validated_data)
def update(self,instance,validated_data):
    instance.user= validated_data.get('user',instance.user)
    instance.userTags= validated_data.get('userTags',instance.userTags)
    instance.applicationID=validated_data.get('applicationID',instance.applicationID)
    instance.deviceDetails= validated_data.get('deviceDetails',instance.deviceDetails)
    instance.applicationFinalReview=validated_data.get('applicationFinalReview',instance.applicationFinalReview)
    instance.appUsedFirstOn=validated_data.get('appUsedFirstOn',instance.appUsedFirstOn)
    instance.save()
    return instance
>>>>>>> bf7a526728ae092050bfe190c6d6e7d19f422281
