from rest_framework import serializers
from .models import *

from user.models import User, Transaksi

class JuriEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = JuriEvent
        fields = '__all__'

class SponsorEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorEvent
        fields = '__all__'

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    kategori = KategoriSerializer(many=True, required=False)
    class Meta:
        model = Event
        fields = '__all__'

class AnggotaGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnggotaGroup
        fields = ['nama']

class GroupEventSerializer(serializers.ModelSerializer):
    anggota = AnggotaGroupSerializer(many=True)
    # user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = GroupEvent
        fields = ['nama', 'total_nominal', 'event', 'anggota','kategori']

    def create(self, validated_data):
        anggota_data = validated_data.pop('anggota')
        kategori_data = validated_data.pop('kategori')
        user = User.objects.get(id=self.context['request'].user.id)
        user.group_event = GroupEvent.objects.create(user=self.context['request'].user,**validated_data)
        user.transaksi = Transaksi.objects.create(status='pembayaran', deskripsi="Pembayaran pendaftaran Event")
        for anggota in anggota_data:
            user.group_event.anggota.create(**anggota)
        user.group_event.kategori = Kategori.objects.get(id=kategori_data)
        user.save()
        return user.group_event
