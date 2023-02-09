from django.urls import path, include
from rest_framework import routers
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()

router.register(r'auth', views.Auth)

urlpatterns = [
    path('', include(router.urls)),
    path('get_provinsi/', views.get_provinsi),
    path('get_kota_kab/', views.get_kota_kab),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
