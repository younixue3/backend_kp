from rest_framework import serializers
from .models import *

from event.serializers import *
import ftplib

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

    # def put(self, validated_data):
    #     FTP_HOST = 'ftp.hbics.sch.id'
    #     FTP_USER = 'u1136649@secondary.hbics.sch.id'
    #     FTP_PASS = 'chc3nskaki'
    #     ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    #     ftp.encoding = 'utf-8'
    #     file_data = validated_data.pop('bukti_pembayaran')
    #     filename = 'file_data.csv'
    #     with open(filename, 'rb') as file:
    #         ftp.storbinary("STOR file_data.csv", filename)
    #     ftp.dir()
    #     print('test')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'no_hp', 'email', 'jenjang', 'asal_sekolah', 'provinsi',
                  'kota_kab']


class ProfileSerializer(serializers.ModelSerializer):
    transaksi = TransaksiSerializer(many=False)
    group_event = GroupEventSerializer(many=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'active', 'first_name', 'last_name', 'jenjang', 'asal_sekolah', 'terverifikasi',
                  'transaksi', 'group_event', 'is_staff']
