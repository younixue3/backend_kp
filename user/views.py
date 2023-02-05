from django.shortcuts import render
from user.models import *

def sync_kota_kab(request):
    provinsi = Provinsi.objects.all()
    for item in provinsi:
        if item.id == 1:
            context = [
                ["kota" : 'Kab. Aceh Barat', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Barat Daya', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Besar', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Jaya', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Selatan', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Singkil', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Tamiang', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Tengah', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Tenggara', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Timur', 'provinsi_id' : 1],
            ["kota" : 'Kab. Aceh Utara', 'provinsi_id' : 1],
            ["kota" : 'Kab. Bener Meriah', 'provinsi_id' : 1],
            ["kota" : 'Kab. Bireuen', 'provinsi_id' : 1],
            ["kota" : 'Kab. Gayo Lues', 'provinsi_id' : 1],
            ["kota" : 'Kab. Nagan Raya', 'provinsi_id' : 1],
            ["kota" : 'Kab. Pidie', 'provinsi_id' : 1],
            ["kota" : 'Kab. Pidie Jaya', 'provinsi_id' : 1],
            ["kota" : 'Kab. Simeulue', 'provinsi_id' : 1],
            ["kota" : 'Kota Banda Aceh', 'provinsi_id' : 1],
            ["kota" : 'Kota Langsa', 'provinsi_id' : 1],
            ["kota" : 'Kota Lhokseumawe', 'provinsi_id' : 1],
            ["kota" : 'Kota Sabang', 'provinsi_id' : 1],
            ["kota" : 'Kota Subulussalam', 'provinsi_id' : 1],
            ]