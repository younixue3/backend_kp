from rest_framework import serializers
from .models import *

from event.serializers import *

class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinsi
        fields = '__all__'
class KotaKabupatenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KotaKabupaten
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'no_hp', 'email', 'jenjang', 'asal_sekolah', 'provinsi', 'kota_kab']

class ProfileSerializer(serializers.ModelSerializer):
    transaksi = TransaksiSerializer(many=False)
    group_event = GroupEventSerializer(many=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'active', 'first_name', 'last_name', 'jenjang', 'asal_sekolah', 'terverifikasi', 'transaksi', 'group_event', 'is_staff']