from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework_simplejwt.tokens import RefreshToken
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
        user.provinsi = Provinsi.objects.get(pk=request.data['provinsi'])
        user.kota_kab = KotaKabupaten.objects.get(pk=request.data['kota'])
        user.save()
        return Response({'type': 'success', 'message': 'Data Prestasi berhasil di simpan'})