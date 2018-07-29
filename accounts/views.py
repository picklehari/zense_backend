from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from tutorial.quickstart.serializers import UserSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =UserSerializer
def accountlist(request):
    if request.method =='GET':
        apps =accounts.objects.all()
        serializer = appSerializer(apps,many=True)
        return JsonResponse(serializer.data ,safe=False)
    elif request.method =='POST':
        data =JSONParser().parse(request)
        serializer = appSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def accountDetails(request,pk):
    try:
        accounts.objects.get(pk=pk)
    except accounts.DoesNotExist:
        return  HttpResponse(status=404)
    if request.method =='GET':
        serializer = appSerializer(accounts)
        return serializer.data
    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = appSerializer(accounts,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=204)
    elif request.method=='DELETE':
        accounts.delete()
        return HttpResponse(status=204)