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

class FrontBeritaPage(ReadOnlyModelViewSet):
    queryset = Berita.objects.order_by('pk')
    serializer_class = FrontBeritaSerializer
    permission_classes = []
    lookup_field = 'slug'

class PengumumanPage(ModelViewSet):
    queryset = Pengumuman.objects.order_by('pk')
    serializer_class = PengumumanSerializer
    permission_classes = [permissions.IsAuthenticated]

class FrontPengumumanPage(ReadOnlyModelViewSet):
    queryset = Pengumuman.objects.order_by('pk')
    serializer_class = FrontPengumumanSerializer
    permission_classes = []
    lookup_field = 'slug'

class FrontImagesPage(ModelViewSet):
    queryset = ImageGaleri.objects.order_by('pk')
    serializer_class = ImageGaleriSerializer
    permission_classes = []
    pagination_class = None

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

class FrontGaleriPage(ModelViewSet):
    queryset = Galeri.objects.order_by('pk')
    serializer_class = FrontGaleriSerialzier
    permission_classes = []

class ImageGaleriPage(ModelViewSet):
    queryset = ImageGaleri.objects.order_by('pk')
    serializer_class = ImageGaleriSerializer
    permission_classes = [permissions.IsAuthenticated]

class TestimoniPage(ModelViewSet):
    queryset = Testimoni.objects.order_by('pk')
    serializer_class = TestimoniSerializer
    permission_classes = [permissions.IsAuthenticated]

class FrontTestimoniPage(ModelViewSet):
    queryset = Testimoni.objects.order_by('pk')
    serializer_class = TestimoniSerializer
    permission_classes = []
    pagination_class = None