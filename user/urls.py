from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'auth', views.Auth)

urlpatterns = [
    path('', include(router.urls)),
    path('get_provinsi/', views.get_provinsi),
    path('get_kota_kab/', views.get_kota_kab),
]
