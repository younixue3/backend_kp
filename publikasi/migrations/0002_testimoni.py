# Generated by Django 4.1.6 on 2023-02-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publikasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimoni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=300)),
                ('testimoni', models.TextField()),
                ('image', models.FileField(upload_to='testimoni/')),
            ],
        ),
    ]