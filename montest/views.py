from telnetlib import STATUS
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *

@api_view(['GET'])
def tachelist(request):
    taches = tache.objects.all()
    serializer = TacheSerial(taches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tachedetail(request, pk):
    taches = tache.objects.get(id=pk)
    serializer = TacheSerial(taches, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def tachecreate(request):
    serial = TacheSerial(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

@api_view(['PUT'])
def tacheupdate(request, pk):
    taches = tache.objects.get(id=pk)
    serial = TacheSerial(instance=taches ,data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

@api_view(['DELETE'])
def tachedelete(request, pk):
    taches = tache.objects.get(id=pk)
    taches.delete()
    return Response(f'element numéro {taches} est suprimé')

