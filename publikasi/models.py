from django.db import models

class Berita(models.Model):
    judul = models.CharField(max_length=150)
    isi = models.TextField()
    file = models.FileField(upload_to='publikasi/berita/', null=True)

class ImageGaleri(models. Model):
    file = models.FileField(upload_to='publikasi/galeri/', null=True)

class Galeri(models.Model):
    tahun = models.CharField(max_length=4)
    image = models.ManyToManyField(ImageGaleri)

class Pengumuman(models.Model):
    judul = models.CharField(max_length=150)
    isi = models.TextField()
    file = models.FileField(upload_to='publikasi/pengumuman/', null=True)