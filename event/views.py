from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view, action

class EventPage(ModelViewSet):
    queryset = Event.objects.order_by('pk')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupEventPage(ModelViewSet):
    queryset = GroupEvent.objects.order_by('pk')
    serializer_class = GroupEventSerializer
    permission_classes = [permissions.IsAuthenticated]

class JuriEventPage(ModelViewSet):
    queryset = JuriEvent.objects.order_by('pk')
    serializer_class = JuriEventSerializer
    permission_classes = [permissions.IsAuthenticated]

class FrontJuriEventPage(ModelViewSet):
    queryset = JuriEvent.objects.order_by('pk')
    serializer_class = JuriEventSerializer
    permission_classes = []
    pagination_class = None

class SponsorEventPage(ModelViewSet):
    queryset = SponsorEvent.objects.order_by('pk')
    serializer_class = SponsorEventSerializer
    permission_classes = [permissions.IsAuthenticated]

class FrontSponsorEventPage(ModelViewSet):
    queryset = SponsorEvent.objects.order_by('pk')
    serializer_class = SponsorEventSerializer
    permission_classes = []
    pagination_class = None