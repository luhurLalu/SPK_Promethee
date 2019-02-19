from django.db import models
from django.contrib.auth.models import User
import time
import os


class Mahasiswa(models.Model):
    # objects = models.Manager()
    nim = models.CharField(max_length=100, blank=True, null=True)
    nama = models.CharField(max_length=100, blank=True, null=True)
    PRIA = 'LAKI-LAKI'
    WANITA = 'PEREMPUAN'
    JK_CHOICES  = (
        (PRIA, 'LAKI-LAKI'),
        (WANITA, 'PEREMPUAN'),

    )
    jenis_kelamin = models.CharField(
        max_length=20,
        choices=JK_CHOICES,
        default=PRIA,
    )
    tgl_lahir = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    agama = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'mahasiswa'
        ordering = ['id']


A   = 'A'
Bb  = 'B+'
B   = 'B'
Cc  = 'C+'
C   = 'C'
D   = 'D'
E   = 'E'
grade  = (        
    (A, 'A'),
    (Bb, 'B+'),
    (B, 'B'),
    (Cc, 'C+'),
    (C, 'C'),
    (D,'D'),
    (E, 'E'),
)         

class Multimedia(models.Model):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE, related_name='multimedias')             

    IMK = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )       
    GrafikaKomputer = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )    
    PrakGrafikaKomputer = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )     
    def __str__(self):
        return self.mahasiswa.nama

    class Meta:
        db_table = 'multimedia'
        ordering = ['id']


class Jaringan(models.Model):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE, related_name='jaringans')    

    Psd = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    Orkom = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    SistemOperasi = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    PrakSistemOperasi = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    Komdat = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    JaringanKomputer = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    PrakJaringanKomputer = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )                
    def __str__(self):
        return self.mahasiswa.nama

    class Meta:
        db_table = 'jaringan'
        ordering = ['id']

class Rpl(models.Model):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE, related_name='rpls')
           
    AlgoritmaDanPemrograman = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    PrakAlgoritmaDanPemrograman = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    PTI = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    StrukturData = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    SistemBasisData = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    PrakSistemBasisData = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    Pemrograman1 = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    PrakPemrograman1 = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    SistemInformasi = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    Pemrograman2 = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    PrakPemrograman2 = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    Adpl = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    ArtificialIntelligent = models.CharField(
        max_length=2,
        choices=grade,
        default=E,
    )
    def __str__(self):
        return self.mahasiswa.nama

    class Meta:
        db_table = 'rpl'
        ordering = ['id']



class Tesdasar(models.Model):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE, related_name='tesdasars')    
    NilaiMultimedia = models.CharField(max_length=2, blank=False, null=True)
    NilaiJaringan = models.CharField(max_length=2, blank=False, null=True)
    NilaiRPL = models.CharField(max_length=2, blank=False, null=True)
    
    def __str__(self):
        return self.mahasiswa.nama

    class Meta: 
        db_table = 'tesdasar'
        ordering = ['id']