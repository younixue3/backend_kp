from django.db import models

class Kategori(models.Model):
    JENJANG_CHOICES = [
        ('smp', 'SMP'),
        ('sma', 'SMA'),
        ('sd', 'SD'),
        ('tk', 'TK')
    ]

    nama = models.CharField(max_length=200)
    nominal = models.IntegerField(null=True)
    jenjang = models.CharField(choices=JENJANG_CHOICES, max_length=3, default='smp')

class Event(models.Model):
    nama = models.CharField(max_length=150)
    deskripsi = models.TextField()
    logo = models.TextField()
    kategori = models.ManyToManyField(Kategori, null=True, blank=False)

class AnggotaGroup(models.Model):
    nama = models.CharField(max_length=100)

class GroupEvent(models.Model):
    nama = models.CharField(max_length=150)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    kategori = models.ForeignKey(Kategori, on_delete=models.DO_NOTHING, blank=True, null=True)
    total_nominal = models.IntegerField(null=True, blank=True)
    anggota = models.ManyToManyField(AnggotaGroup)

class JuriEvent(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField()
    image = models.TextField()
    video = models.TextField()

class SponsorEvent(models.Model):
    nama = models.CharField(max_length=100)
    logo = models.TextField()