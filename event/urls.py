from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'event', views.EventPage)
router.register(r'group-event', views.GroupEventPage)
router.register(r'juri', views.JuriEventPage)
router.register(r'sponsor', views.SponsorEventPage)
router.register(r'front-juri', views.FrontJuriEventPage)
router.register(r'front-sponsor', views.FrontSponsorEventPage)

urlpatterns = [
    path('', include(router.urls)),
]
