from django.db import models
from django.utils.text import slugify


class Berita(models.Model):
    judul = models.CharField(max_length=150)
    slug = models.SlugField(null=True)
    isi = models.TextField()
    file = models.TextField()
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

class ImageGaleri(models. Model):
    file = models.TextField()

class Galeri(models.Model):
    tahun = models.CharField(max_length=4)
    image = models.ManyToManyField(ImageGaleri)

class Testimoni(models.Model):
    nama = models.CharField(max_length=300)
    testimoni = models.TextField()
    image = models.TextField()

class Pengumuman(models.Model):
    judul = models.CharField(max_length=150)
    slug = models.SlugField(null=True)
    isi = models.TextField()
    file = models.TextField()
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)