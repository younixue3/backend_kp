from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission, User
from django.db import models
from django.utils import timezone
import uuid

class User(AbstractUser):
    uniid = models.UUIDField(default=uuid.uuid4(), editable=False)

class Provinsi(models.Model):
    provinsi = models.CharField(max_length=50)

class KotaKabupaten(models.Model):
    kota = models.CharField(max_length=50)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)