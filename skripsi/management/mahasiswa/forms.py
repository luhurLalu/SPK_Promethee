from django import forms
from orm.models import Mahasiswa,Jaringan,Rpl,Multimedia,Tesdasar

class MahasiswaForm(forms.Form):
    nim = forms.IntegerField(initial=0)
    nama = forms.CharField(max_length=50)
    jenis_kelamin = forms.CharField(max_length=20)
    tgl_lahir = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    agama = forms.CharField(max_length=20)

OPTIONS = (
    ('A', 'A'),
    ('Bb', 'B+'),
    ('B', 'B'),
    ('Cc', 'C+'),
    ('C', 'C'),
    ('D','D')
)
class MultimediaForm(forms.Form):
    IMK = forms.CharField(max_length=4)    
    GrafikaKomputer = forms.CharField(max_length=4)
    PrakGrafikaKomputer = forms.CharField(max_length=4)

class JaringanForm(forms.Form):
    Psd = forms.CharField(max_length=4)
    Orkom = forms.CharField(max_length=4)
    SistemOperasi = forms.CharField(max_length=4)
    PrakSistemOperasi = forms.CharField(max_length=4)
    Komdat = forms.CharField(max_length=4)
    JaringanKomputer = forms.CharField(max_length=4)
    PrakJaringanKomputer = forms.CharField(max_length=4)

class RplForm(forms.Form):
    AlgoritmaDanPemrograman = forms.CharField(max_length=4)
    PrakAlgoritmaDanPemrograman = forms.CharField(max_length=4)
    PTI = forms.CharField(max_length=4)
    StrukturData = forms.CharField(max_length=4)
    SistemBasisData = forms.CharField(max_length=4)
    PrakSistemBasisData = forms.CharField(max_length=4)
    Pemrograman1 = forms.CharField(max_length=4)
    PrakPemrograman1 = forms.CharField(max_length=4)
    SistemInformasi = forms.CharField(max_length=4)
    Pemrograman2 = forms.CharField(max_length=4)
    PrakPemrograman2 = forms.CharField(max_length=4)
    Adpl = forms.CharField(max_length=4)    
    ArtificialIntelligent = forms.CharField(max_length=4)

class TesDasarForm(forms.Form):
    NilaiMultimedia = forms.IntegerField(initial=0)
    NilaiJaringan = forms.IntegerField(initial=0)
    NilaiRPL = forms.IntegerField(initial=0)

    class Meta:
        model = Mahasiswa