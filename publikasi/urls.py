from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'berita', views.BeritaPage)
router.register(r'front-berita', views.FrontBeritaPage)
router.register(r'pengumuman', views.PengumumanPage)
router.register(r'front-pengumuman', views.FrontPengumumanPage)
router.register(r'galeri', views.GaleriPage)
router.register(r'front-galeri', views.FrontGaleriPage)
router.register(r'image-galeri', views.ImageGaleriPage)
router.register(r'front-images', views.FrontImagesPage)
router.register(r'testimoni', views.TestimoniPage)
router.register(r'front-testimoni', views.FrontTestimoniPage)

urlpatterns = [
    path('', include(router.urls)),
]
