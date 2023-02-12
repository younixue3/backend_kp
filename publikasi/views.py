from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view, action

class BeritaPage(ModelViewSet):
    queryset = Berita.objects.order_by('pk')
    serializer_class = BeritaSerializer
    permission_classes = [permissions.IsAuthenticated]

    # @action(methods=['POST'], detail=False)
    # def insertBerita(self, request):
    #     print(request.data)
    #     berita = self.queryset.create(
    #         judul=request.data['judul'],
    #         isi = request.data['isi'],
    #         file = request.data['file']
    #     )
    #     serializer = self.serializer_class(berita, many=False, context={'request': request})
    #     return Response(serializer.data)
    # @action(methods=['POST'], detail=True)
    # def updateBerita(self, request, pk=None):
    #     print(request.data)
    #     berita = Berita.objects.get(id=pk)
    #     print(berita)
class PengumumanPage(ModelViewSet):
    queryset = Pengumuman.objects.order_by('pk')
    serializer_class = PengumumanSerializer
    permission_classes = [permissions.IsAuthenticated]

    # @action(methods=['POST'], detail=False)
    # def insertPengumuman(self, request):
    #     print(request.data)
    #     berita = self.queryset.create(
    #         judul=request.data['judul'],
    #         isi=request.data['isi'],
    #         file=request.data['file']
    #     )
    #     serializer = self.serializer_class(berita, many=False, context={'request': request})
    #     return Response(serializer.data)
class GaleriPage(ModelViewSet):
    queryset = Galeri.objects.order_by('pk')
    serializer_class = GaleriSerialzier
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['POST'], detail=False)
    def insertGaleri(self, request):
        print(request.data)
        galeri = self.queryset.create(
            tahun=request.data['tahun']
        )
        serializer = self.serializer_class(galeri, many=False, context={'request': request})
        return Response(serializer.data)

    @action(methods=['PUT'], detail=True)
    def updateGaleri(self, request, pk=None):
        print(request.data)
        galeri = self.queryset.get(id=pk)
        galeri.tahun = request.data['tahun']
        for item in request.FILES:
            galeri.image.create(file=request.FILES[item])
        galeri.save()
        serializer = self.serializer_class(galeri, context={'request': request})
        return Response(serializer.data)

class ImageGaleriPage(ModelViewSet):
    queryset = ImageGaleri.objects.order_by('pk')
    serializer_class = ImageGaleriSerializer
    permission_classes = [permissions.IsAuthenticated]