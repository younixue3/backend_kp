from django.urls import path, include
from rest_framework import routers
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()

router.register(r'berita', views.BeritaPage)
router.register(r'pengumuman', views.PengumumanPage)
router.register(r'galeri', views.GaleriPage)
router.register(r'image-galeri', views.ImageGaleriPage)

urlpatterns = [
    path('', include(router.urls)),
]
