from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'event', views.EventPage)
router.register(r'group-event', views.GroupEventPage)

urlpatterns = [
    path('', include(router.urls)),
]
