from django.db import models
from django.utils.text import slugify


class Berita(models.Model):
    judul = models.CharField(max_length=150)
    slug = models.SlugField(null=True)
    isi = models.TextField()
    file = models.FileField(upload_to='media/publikasi/berita/', null=True)
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

class ImageGaleri(models. Model):
    file = models.FileField(upload_to='media/publikasi/galeri/', null=True)

class Galeri(models.Model):
    tahun = models.CharField(max_length=4)
    image = models.ManyToManyField(ImageGaleri)

class Testimoni(models.Model):
    nama = models.CharField(max_length=300)
    testimoni = models.TextField()
    image = models.FileField(upload_to='media/publikasi/testimoni/')

class Pengumuman(models.Model):
    judul = models.CharField(max_length=150)
    slug = models.SlugField(null=True)
    isi = models.TextField()
    file = models.FileField(upload_to='media/publikasi/pengumuman/', null=True)
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)