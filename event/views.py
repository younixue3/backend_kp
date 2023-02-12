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
    permission_classes = []