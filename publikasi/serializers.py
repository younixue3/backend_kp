from rest_framework import serializers
from .models import *

class BeritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berita
        fields = '__all__'

class PengumumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengumuman
        fields = '__all__'

class ImageGaleriSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGaleri
        fields = '__all__'

class GaleriSerialzier(serializers.ModelSerializer):
    image = ImageGaleriSerializer(many=True)
    class Meta:
        model = Galeri
        fields = '__all__'