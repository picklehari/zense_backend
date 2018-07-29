from rest_framework import serializers
from .models import developer
class developerSerializer(serializers.Serializer):
    class Meta:
        model = developer
        field = ('user','devID')
    def create(self,validated_data):
        return developer.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.user = validated_data.get('user',instance.user)
        instance.devID = validated_data.get('devID',,instance.devID)
        instance.save()
        return instance
    