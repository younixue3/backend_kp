from django.db import models

class Event(models.Model):
    nama = models.CharField(max_length=150)
    deskripsi = models.TextField()
    logo = models.FileField(upload_to='event/logo/', null=True)
    nominal = models.IntegerField()
class AnggotaGroup(models.Model):
    nama = models.CharField(max_length=100)

class GroupEvent(models.Model):
    nama = models.CharField(max_length=150)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    total_nominal = models.IntegerField()
    anggota = models.ManyToManyField(AnggotaGroup)
