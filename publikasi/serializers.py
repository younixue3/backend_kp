from rest_framework import serializers
from .models import *

class BeritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berita
        fields = '__all__'

class FrontBeritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berita
        lookup_field = 'slug'
        fields = '__all__'

class PengumumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengumuman
        fields = '__all__'

class FrontPengumumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengumuman
        lookup_field = 'slug'
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

class FrontGaleriSerialzier(serializers.ModelSerializer):
    image = ImageGaleriSerializer(many=True)
    image_count = serializers.IntegerField(
        source='image.count',
        read_only=True
    )
    class Meta:
        model = Galeri
        fields = '__all__'

class TestimoniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimoni
        fields = '__all__'