from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
class AnggotaGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnggotaGroup
        fields = '__all__'