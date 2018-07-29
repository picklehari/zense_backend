from django.contrib.auth.models import User
from rest_framework import serializers
from .models import userProfile
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email')

class profileSerializer(serializers.Serializer):
    class Meta:
        model = userProfile
        field= ('user','userTags','applicationID','deviceDetails','appUsedFirstOn','applicationFinalReview')
        