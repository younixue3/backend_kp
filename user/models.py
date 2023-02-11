from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission, User
from django.db import models
from django.utils import timezone
import uuid


class Provinsi(models.Model):
    provinsi = models.CharField(max_length=50)


class KotaKabupaten(models.Model):
    kota = models.CharField(max_length=50)

class User(AbstractUser):

    JENJANG_CHOICES = [
        ('smp', 'SMP'),
        ('sma', 'SMA'),
        ('sd', 'SD'),
        ('tk', 'TK')
    ]

    uniid = models.UUIDField(default=uuid.uuid4(), editable=False)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE, default=15)
    kota_kab = models.ForeignKey(KotaKabupaten, on_delete=models.CASCADE, default=189)
    no_hp = models.CharField(max_length=18, null=True)
    jenjang = models.CharField(choices=JENJANG_CHOICES, max_length=3, default='smp')
    active = models.BooleanField(default=False)
