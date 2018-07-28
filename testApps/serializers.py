from rest_framework import serializers
from .models import testApp 
class appSerializer(serializers.Serializer):
    class Meta:
        model = testApp
        field = ('applicationID','applicationName','applicationDescription','applicationDownloads','uploaderID','applicationVerdict','applicationPartsToReview')
    def create(self,validated_data):
        return testApp.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.applicationID = validated_data.get('applicationID',instance.applicationID)
        instance.applicationName = validated_data.get('applicationName',instance.applicationName)
        instance.applicationDescription = validated_data.get('applicationDescription',instance.applicationDescription)
        instance.applicationDownloads = validated_data.get('applicationDownloads',instance.applicationDownloads)
        instance.uploaderID = validated_data.get('uploaderID',instance.uploaderID)
        instance.applicationVerdict = validated_data.get('applicationVerdict',instance.applicationVerdict)
        instance.applicationPartsToReview = validated_data.get('applicationPartsToReview',instance.applicationPartsToReview)
        instance.save()
        return instance