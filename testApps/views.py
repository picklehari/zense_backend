from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import testApp
from .serializers import appSerializer
<<<<<<< HEAD
=======

>>>>>>> bf7a526728ae092050bfe190c6d6e7d19f422281
@csrf_exempt
def applist(request):
    if request.method =='GET':
        apps =testApp.objects.all()
        serializer = appSerializer(apps,many=True)
        return JsonResponse(serializer.data ,safe=False)
    elif request.method =='POST':
        data =JSONParser().parse(request)
        serializer = appSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

def appDetails(request,pk):
    try:
        testApp.objects.get(pk=pk)
    except testApp.DoesNotExist:
        return  HttpResponse(status=404)
    if request.method =='GET':
        serializer = appSerializer(testApp)
        return serializer.data
    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = appSerializer(testApp,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=204)
    elif request.method=='DELETE':
        testApp.delete()
        return HttpResponse(status=204)
