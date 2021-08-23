from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from user import models
from . import serializers

# Create your views here.

class ListUser(generics.ListCreateAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

@api_view(['POST',])
@permission_classes((AllowAny, ))
def registration_view(request):
    if request.method == 'POST':
        serializer = serializers.RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Berhasil terdaftar'
            data['username'] = account.username
        else:
            data = serializer.is_errors
        return Response(data)

@api_view(['POST',])
@permission_classes((AllowAny, ))
def absen_view(request):
    if request.method == 'POST':
        serializer = serializers.AbsenSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            absen = serializer.save()
            data['response'] = 'Berhasil absen'
            data['name'] = absen.name
        else:
            data = serializer.is_errors
        return Response(data)