from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Mahasiswa,Multimedia,Jaringan,Rpl,Tesdasar
from management.mahasiswa import helpers
from management.mahasiswa.forms import MahasiswaForm,MultimediaForm,JaringanForm,RplForm,TesDasarForm
from django.contrib.auth.mixins import LoginRequiredMixin
import mimetypes
import os

# Create your views here.
mhs = Mahasiswa.objects.all()

class HomeView(View):
    def get(self, request):
        template = 'mahasiswa/home.html'
        return render(request,template)
        
class ListMahasiswaView(View):
    def get(self, request):
        template = 'mahasiswa/index.html'
        mahasiswa = Mahasiswa.objects.all()
        data = {
            'mahasiswa' : mahasiswa,
        }
        return render(request, template, data)

class ListHasilRekomendasiMahasiswa(View):
    def get(self, request):        
        template = 'mahasiswa/data_rekomendasi.html'
        data_rekomendasi = helpers.Induk()[0].as_matrix()
        data = { 
            'data_rekomendasi': data_rekomendasi
        }
        return render(request, template, data)
    
class ListAkademikMahasiswa(View):
    def get(self,request):        
        template = 'mahasiswa/kriteria/akademik.html'        
        akademik = helpers.Induk()[1].as_matrix()
        data = {            
            'akademik' : akademik
        }
        return render(request,template,data)

class ListTestMahasiswa(View):
    def get(self,request):                
        template = 'mahasiswa/kriteria/tes_dasar.html'
        tesdasar = helpers.Induk()[2].as_matrix()        
        data = {            
            'tesdasar' : tesdasar
        }
        return render(request,template,data)

class ListDetailMahasiswa(View):
    def get(self,request,id):        
        template = 'mahasiswa/detail_promethee.html' 
        pr = helpers.Induk()[3]
        detail_mahasiswa = pr[int(id)-1].as_matrix()        
        nama_mhs = helpers.Induk()[4].as_matrix()[0][int(id)-1] 
        # mhs = Mahasiswa.objects.get(id=id)
        data = {      

            'detail_mahasiswa' : detail_mahasiswa,
            'mahasiswa': nama_mhs
        }
        return render(request,template,data)

class EditView(View):
    def get(self, request, id):
        fltr = Mahasiswa.objects.filter(id=id)
        if not fltr.exists():
            return redirect('mahasiswa:view')
        mhs = fltr.first()
        initial = {
            'id': mhs.id,            
            'tanggal_lahir': mhs.tgl_lahir,
        }

        form = MahasiswaForm(initial=initial)
        template = 'mahasiswa/crud/update.html'
        data = {
            'form': form,
            'mahasiswa': Mahasiswa.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateView(View):
    def post(self, request, id):
        mahasiswa = Mahasiswa.objects.get(id=id)
        
        mahasiswa_form = MahasiswaForm(request.POST or None, request.FILES)
        multimedia_form = MultimediaForm(request.POST or None)
        jaringan_form = JaringanForm(request.POST or None)
        rpl_form = RplForm(request.POST or None)
        tesdasar_form = TesDasarForm(request.POST or None)        

        if mahasiswa_form.is_valid() and multimedia_form.is_valid() and jaringan_form.is_valid() and rpl_form.is_valid() and tesdasar_form.is_valid():

            mahasiswa.nim = mahasiswa_form.cleaned_data['nim']
            mahasiswa.nama = mahasiswa_form.cleaned_data['nama']
            mahasiswa.jenis_kelamin = mahasiswa_form.cleaned_data['jenis_kelamin']
            mahasiswa.tgl_lahir = mahasiswa_form.cleaned_data['tgl_lahir']
            mahasiswa.agama = mahasiswa_form.cleaned_data['agama']
            mahasiswa.save(force_update=True)
                        
            mahasiswa.multimedias.IMK = multimedia_form.cleaned_data['IMK']            
            mahasiswa.multimedias.GrafikaKomputer = multimedia_form.cleaned_data['GrafikaKomputer']
            mahasiswa.multimedias.PrakGrafikaKomputer = multimedia_form.cleaned_data['PrakGrafikaKomputer']
            mahasiswa.multimedias.save(force_update=True)
                        
            mahasiswa.jaringans.Psd = jaringan_form.cleaned_data['Psd']
            mahasiswa.jaringans.Orkom = jaringan_form.cleaned_data['Orkom']
            mahasiswa.jaringans.SistemOperasi = jaringan_form.cleaned_data['SistemOperasi']
            mahasiswa.jaringans.PrakSistemOperasi = jaringan_form.cleaned_data['PrakSistemOperasi']
            mahasiswa.jaringans.Komdat = jaringan_form.cleaned_data['Komdat']
            mahasiswa.jaringans.JaringanKomputer = jaringan_form.cleaned_data['JaringanKomputer']
            mahasiswa.jaringans.PrakJaringanKomputer = jaringan_form.cleaned_data['PrakJaringanKomputer']
            mahasiswa.jaringans.save(force_update=True)
                        
            mahasiswa.rpls.AlgoritmaDanPemrograman = rpl_form.cleaned_data['AlgoritmaDanPemrograman']
            mahasiswa.rpls.PrakAlgoritmaDanPemrograman = rpl_form.cleaned_data['PrakAlgoritmaDanPemrograman']
            mahasiswa.rpls.PTI = rpl_form.cleaned_data['PTI']
            mahasiswa.rpls.StrukturData = rpl_form.cleaned_data['StrukturData']
            mahasiswa.rpls.SistemBasisData = rpl_form.cleaned_data['SistemBasisData']
            mahasiswa.rpls.PrakSistemBasisData = rpl_form.cleaned_data['PrakSistemBasisData']
            mahasiswa.rpls.Pemrograman1 = rpl_form.cleaned_data['Pemrograman1']
            mahasiswa.rpls.PrakPemrograman1 = rpl_form.cleaned_data['PrakPemrograman1']
            mahasiswa.rpls.SistemInformasi = rpl_form.cleaned_data['SistemInformasi']
            mahasiswa.rpls.Pemrograman2 = rpl_form.cleaned_data['Pemrograman2']
            mahasiswa.rpls.PrakPemrograman2 = rpl_form.cleaned_data['PrakPemrograman2']
            mahasiswa.rpls.Adpl = rpl_form.cleaned_data['Adpl']
            mahasiswa.rpls.ArtificialIntelligent = rpl_form.cleaned_data['ArtificialIntelligent']
            mahasiswa.rpls.save(force_update=True)
                        
            mahasiswa.tesdasars.NilaiMultimedia = tesdasar_form.cleaned_data['NilaiMultimedia']
            mahasiswa.tesdasars.NilaiJaringan = tesdasar_form.cleaned_data['NilaiJaringan']
            mahasiswa.tesdasars.NilaiRPL = tesdasar_form.cleaned_data['NilaiRPL']
            mahasiswa.tesdasars.save(force_update=True)

            # messages.add_message(request,messages.INFO, 'Tambah Data Sukses!')

            return redirect('mahasiswa:mahasiswa')
        else:
            return HttpResponse(mahasiswa_form.errors)

class ViewDataView(View):
    def get(self, request, id):
        fltr = Mahasiswa.objects.filter(id=id)
        if not fltr.exists():
            return redirect('mahasiswa:mahasiswa')
        mhs = fltr.first()
        initial = {
            'id' : mhs.id,            
        }
        form = MahasiswaForm(initial=initial)
        template = 'mahasiswa/crud/read.html'
        data = {
            'form' : form,
            'mahasiswa': Mahasiswa.objects.get(id=id),            
        }
        return render(request, template,data)

# class ReadDataView(View):
#     def post(self, request, id):
#         mahasiswa = Mahasiswa.objects.get(id=id)
        
#         mahasiswa_form = MahasiswaForm(request.POST or None, request.FILES)
#         multimedia_form = MultimediaForm(request.POST or None)
#         jaringan_form = JaringanForm(request.POST or None)
#         rpl_form = RplForm(request.POST or None)
#         tesdasar_form = TesDasarForm(request.POST or None)        

#         if mahasiswa_form.is_valid() and multimedia_form.is_valid() and jaringan_form.is_valid() and rpl_form.is_valid() and tesdasar_form.is_valid():

#             mahasiswa.nim = mahasiswa_form.cleaned_data['nim']
#             mahasiswa.nama = mahasiswa_form.cleaned_data['nama']
#             mahasiswa.jenis_kelamin = mahasiswa_form.cleaned_data['jenis_kelamin']
#             mahasiswa.tgl_lahir = mahasiswa_form.cleaned_data['tgl_lahir']
#             mahasiswa.agama = mahasiswa_form.cleaned_data['agama']
#             mahasiswa.save(force_update=True)
                        
#             mahasiswa.multimedias.IMK = multimedia_form.cleaned_data['IMK']            
#             mahasiswa.multimedias.GrafikaKomputer = multimedia_form.cleaned_data['GrafikaKomputer']
#             mahasiswa.multimedias.PrakGrafikaKomputer = multimedia_form.cleaned_data['PrakGrafikaKomputer']
#             mahasiswa.multimedias.save(force_update=True)
                        
#             mahasiswa.jaringans.Psd = jaringan_form.cleaned_data['Psd']
#             mahasiswa.jaringans.Orkom = jaringan_form.cleaned_data['Orkom']
#             mahasiswa.jaringans.SistemOperasi = jaringan_form.cleaned_data['SistemOperasi']
#             mahasiswa.jaringans.PrakSistemOperasi = jaringan_form.cleaned_data['PrakSistemOperasi']
#             mahasiswa.jaringans.Komdat = jaringan_form.cleaned_data['Komdat']
#             mahasiswa.jaringans.JaringanKomputer = jaringan_form.cleaned_data['JaringanKomputer']
#             mahasiswa.jaringans.PrakJaringanKomputer = jaringan_form.cleaned_data['PrakJaringanKomputer']
#             mahasiswa.jaringans.save(force_update=True)
                        
#             mahasiswa.rpls.AlgoritmaDanPemrograman = rpl_form.cleaned_data['AlgoritmaDanPemrograman']
#             mahasiswa.rpls.PrakAlgoritmaDanPemrograman = rpl_form.cleaned_data['PrakAlgoritmaDanPemrograman']
#             mahasiswa.rpls.PTI = rpl_form.cleaned_data['PTI']
#             mahasiswa.rpls.StrukturData = rpl_form.cleaned_data['StrukturData']
#             mahasiswa.rpls.SistemBasisData = rpl_form.cleaned_data['SistemBasisData']
#             mahasiswa.rpls.PrakSistemBasisData = rpl_form.cleaned_data['PrakSistemBasisData']
#             mahasiswa.rpls.Pemrograman1 = rpl_form.cleaned_data['Pemrograman1']
#             mahasiswa.rpls.PrakPemrograman1 = rpl_form.cleaned_data['PrakPemrograman1']
#             mahasiswa.rpls.SistemInformasi = rpl_form.cleaned_data['SistemInformasi']
#             mahasiswa.rpls.Pemrograman2 = rpl_form.cleaned_data['Pemrograman2']
#             mahasiswa.rpls.PrakPemrograman2 = rpl_form.cleaned_data['PrakPemrograman2']
#             mahasiswa.rpls.Adpl = rpl_form.cleaned_data['Adpl']
#             mahasiswa.rpls.ArtificialIntelligent = rpl_form.cleaned_data['ArtificialIntelligent']
#             mahasiswa.rpls.save(force_update=True)
                        
#             mahasiswa.tesdasars.NilaiMultimedia = tesdasar_form.cleaned_data['NilaiMultimedia']
#             mahasiswa.tesdasars.NilaiJaringan = tesdasar_form.cleaned_data['NilaiJaringan']
#             mahasiswa.tesdasars.NilaiRPL = tesdasar_form.cleaned_data['NilaiRPL']
#             mahasiswa.tesdasars.save(force_update=True)            

#             return redirect('mahasiswa:mahasiswa')
#         else:
#             return HttpResponse(mahasiswa_form.errors)

class HapusView(View):
    def get(self, request, idMhs):
        mhs = Mahasiswa.objects.get(id=idMhs)
        mhs.delete()
        
        messages.warning(request,'Hapus Data Berhasil !')
        return redirect('mahasiswa:mahasiswa')
 
class TambahDataView(View):
    def post(self,request):
        mahasiswa_form = MahasiswaForm(request.POST or None)
        multimedia_form = MultimediaForm(request.POST or None)
        jaringan_form = JaringanForm(request.POST or None)
        rpl_form = RplForm(request.POST or None)
        tesdasar_form = TesDasarForm(request.POST or None)

        if mahasiswa_form.is_valid() and multimedia_form.is_valid() and jaringan_form.is_valid() and rpl_form.is_valid() and tesdasar_form.is_valid():
            mahasiswa = Mahasiswa()
            mahasiswa.nim = mahasiswa_form.cleaned_data['nim']
            mahasiswa.nama = mahasiswa_form.cleaned_data['nama']
            mahasiswa.jenis_kelamin = mahasiswa_form.cleaned_data['jenis_kelamin']
            mahasiswa.tgl_lahir = mahasiswa_form.cleaned_data['tgl_lahir']
            mahasiswa.agama = mahasiswa_form.cleaned_data['agama']
            mahasiswa.save()

            multimedia = Multimedia() 
            multimedia.mahasiswa = mahasiswa
            multimedia.IMK = multimedia_form.cleaned_data['IMK']            
            multimedia.GrafikaKomputer = multimedia_form.cleaned_data['GrafikaKomputer']
            multimedia.PrakGrafikaKomputer = multimedia_form.cleaned_data['PrakGrafikaKomputer']
            multimedia.save()

            jaringan = Jaringan()
            jaringan.mahasiswa = mahasiswa
            jaringan.Psd = jaringan_form.cleaned_data['Psd']
            jaringan.Orkom = jaringan_form.cleaned_data['Orkom']
            jaringan.SistemOperasi = jaringan_form.cleaned_data['SistemOperasi']
            jaringan.PrakSistemOperasi = jaringan_form.cleaned_data['PrakSistemOperasi']
            jaringan.Komdat = jaringan_form.cleaned_data['Komdat']
            jaringan.JaringanKomputer = jaringan_form.cleaned_data['JaringanKomputer']
            jaringan.PrakJaringanKomputer = jaringan_form.cleaned_data['PrakJaringanKomputer']
            jaringan.save()

            rpl = Rpl()
            rpl.mahasiswa = mahasiswa
            rpl.AlgoritmaDanPemrograman = rpl_form.cleaned_data['AlgoritmaDanPemrograman']
            rpl.PrakAlgoritmaDanPemrograman = rpl_form.cleaned_data['PrakAlgoritmaDanPemrograman']
            rpl.PTI = rpl_form.cleaned_data['PTI']
            rpl.StrukturData = rpl_form.cleaned_data['StrukturData']
            rpl.SistemBasisData = rpl_form.cleaned_data['SistemBasisData']
            rpl.PrakSistemBasisData = rpl_form.cleaned_data['PrakSistemBasisData']
            rpl.Pemrograman1 = rpl_form.cleaned_data['Pemrograman1']
            rpl.PrakPemrograman1 = rpl_form.cleaned_data['PrakPemrograman1']
            rpl.SistemInformasi = rpl_form.cleaned_data['SistemInformasi']
            rpl.Pemrograman2 = rpl_form.cleaned_data['Pemrograman2']
            rpl.PrakPemrograman2 = rpl_form.cleaned_data['PrakPemrograman2']
            rpl.Adpl = rpl_form.cleaned_data['Adpl']
            rpl.ArtificialIntelligent = rpl_form.cleaned_data['ArtificialIntelligent']
            rpl.save()

            tesdasar = Tesdasar()
            tesdasar.mahasiswa = mahasiswa
            tesdasar.NilaiMultimedia = tesdasar_form.cleaned_data['NilaiMultimedia']
            tesdasar.NilaiJaringan = tesdasar_form.cleaned_data['NilaiJaringan']
            tesdasar.NilaiRPL = tesdasar_form.cleaned_data['NilaiRPL']
            tesdasar.save()

            messages.add_message(request,messages.INFO, 'Tambah Data Sukses!')
            # messages.success(request,'Form Berhasil Bekerja')

            return redirect('mahasiswa:mahasiswa')
        else:
            return HttpResponse(mahasiswa_form.errors and multimedia_form.errors and jaringan_form.errors and rpl_form.errors and tesdasar_form.errors)
