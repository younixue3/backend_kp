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

class JuriEvent(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField()
    image = models.FileField(upload_to='juri/foto/', null=True)
    video = models.FileField(upload_to='juri/video/', null=True)

class SponsorEvent(models.Model):
    nama = models.CharField(max_length=100)
    logo = models.FileField(upload_to='event/sponsor/', null=True)