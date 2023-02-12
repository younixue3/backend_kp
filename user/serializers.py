from rest_framework import serializers
from .models import *

class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinsi
        fields = '__all__'
class KotaKabupatenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KotaKabupaten
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'activez']