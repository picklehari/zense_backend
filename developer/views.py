from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import developer
from .serializers import developerSerializer

@csrf_exempt
def applist(request):
    if request.method =='GET':
        devs =developer.objects.all()
        serializer = developerSerializer(devs,many=True)
        return JsonResponse(serializer.data ,safe=False)
    elif request.method =='POST':
        data =JSONParser().parse(request)
        serializer = developerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

def appDetails(request,pk):
    try:
        developer.objects.get(pk=pk)
    except developer.DoesNotExist:
        return  HttpResponse(status=404)
    if request.method =='GET':
        serializer = developerSerializer(developer)
        return serializer.data
    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = developerSerializer(developer,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=204)
    elif request.method=='DELETE':
        developer.delete()
        return HttpResponse(status=204)
