import json

from django.core import serializers as s

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from user import models
from . import serializers

# Create your views here.

class ListUser(generics.ListCreateAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer


class DetailUser(APIView):
    def post(self, request):
        # Data post
        uname = request.data['username']

        # Get all object absen and take name with Data post
        json_absen = json.loads(s.serialize('json', models.Absen.objects.all()))
        array_absen = []
        for i in json_absen:
            if i['fields']['name'] == uname:
                array_absen.append(i['fields'])

        # Get object with name
        json_qs = json.loads(s.serialize('json', models.Account.objects.filter(username=uname)))[0]['fields']
        json_qs['absen'] = array_absen
        result = json_qs

        return Response(result)

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