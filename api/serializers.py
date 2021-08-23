from rest_framework import serializers
from user import models


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'name',
            'is_guru',
            'is_dudi',
            'is_superuser',
            'longitude',
            'latitude',
            'absen'
        )
        model = models.Account

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = models.Account
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        account = models.Account(
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise  serializers.ValidationError({'password': 'Password tidak sama'})
        account.set_password(password)
        account.save()
        return account


class AbsenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Absen
        fields = ['name', 'longitude', 'latitude']
    
    def save(self):
        absen = models.Absen(
            name=self.validated_data['name'],
            longitude=self.validated_data['longitude'],
            latitude=self.validated_data['latitude']
        )
        absen.save()
        return absen