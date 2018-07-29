from django.contrib.auth.models import User
from rest_framework import serializers
from .models import userProfile
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email')
def create(self,validated_data):
    return userProfile.objects.create(**validated_data)
def update(self,instance,validated_data):
    
