from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class AnggotaGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnggotaGroup
        fields = ['nama']

class GroupEventSerializer(serializers.ModelSerializer):
    anggota = AnggotaGroupSerializer(many=True)
    class Meta:
        model = GroupEvent
        fields = ['nama', 'total_nominal', 'event', 'anggota']

    def create(self, validated_data):
        anggota_data = validated_data.pop('anggota')
        groupevent = GroupEvent.objects.create(**validated_data)
        for anggota in anggota_data:
            groupevent.anggota.create(**anggota)
            # AnggotaGroup.objects.create(groupevent=groupevent, **anggota)
        return groupevent