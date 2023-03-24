from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import permissions
from rest_framework_simplejwt.backends import TokenBackend

@api_view(['POST'])
def get_profile(request):
    valid_data = AccessToken(request.data['access'])
    print(valid_data['user_id'])
    user = User.objects.get(pk=valid_data['user_id'])
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)
@api_view(['GET'])
def get_provinsi(request):
    provinsi = Provinsi.objects.all()
    serializer = ProvinsiSerializer(provinsi, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_kota_kab(request):
    kota_kab = KotaKabupaten.objects.all()
    serializer = KotaKabupatenSerializer(kota_kab, many=True)
    return Response(serializer.data)

class TransaksiPage(ModelViewSet):
    queryset = Transaksi.objects.order_by('pk')
    serializer_class = TransaksiSerializer
    permission_classes = []

    @action(methods=['POST'], detail=False)
    def testftp(self, request):
        FTP_HOST = 'ftp.hbics.sch.id'
        FTP_USER = 'u1136649@secondary.hbics.sch.id'
        FTP_PASS = 'chc3nskaki'
        ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
        ftp.encoding = 'utf-8'
        file_data = request.FILES['file']
        print(file_data)
        filename = file_data
        with open(filename, 'rb') as file:
            ftp.storbinary('STOR' + filename, filename)
        ftp.dir()
        print('test')

class PesertaPage(ModelViewSet):
    queryset = User.objects.filter(is_staff=False).order_by('pk')
    serializer_class = ProfileSerializer
    permission_classes = []

class Auth(ReadOnlyModelViewSet):
    queryset = User.objects.order_by('pk')
    serializer_class = UserSerializer
    permission_classes = []
    @action(methods=['POST'], detail=False)
    def registerAccount(self, request):
        user = User()
        user.username = request.data['email']
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.no_hp = request.data['no_hp']
        user.email = request.data['email']
        user.set_password(request.data['password'])
        user.jenjang = request.data['jenjang']
        user.asal_sekolah = request.data['asal_sekolah']
        user.provinsi = Provinsi.objects.get(pk=request.data['provinsi'])
        user.kota_kab = KotaKabupaten.objects.get(pk=request.data['kota'])
        user.save()
        return Response({'type': 'success', 'message': 'Data Prestasi berhasil di simpan'})