import os, django
import pandas as pd
from orm.models import Mahasiswa,Jaringan,Rpl,Multimedia,Tesdasar
import math
import operator

def Induk():
    mhs = Mahasiswa.objects.all()
    mul = Multimedia.objects.all()
    rpl = Rpl.objects.all()
    jar = Jaringan.objects.all()
    tes = Tesdasar.objects.all()

    def Orang(mhs):
        # a = pd.DataFrame([enumerate(mhs)])
        a = pd.DataFrame([mhs])
        return a

    if len(mhs)>0:
        colsm = ['Interaksi Manusia Dan Komputer','Grafika Komputer',
                'Prak.Grafika Komputer']

        kelm ={
            colsm[0] : [str(a.multimedias.IMK) for a in mhs],        
            colsm[1] : [str(a.multimedias.GrafikaKomputer) for a in mhs],
            colsm[2] : [str(a.multimedias.PrakGrafikaKomputer) for a in mhs],            
        }
        dfm = pd.DataFrame(data=kelm)
    else:
        dfm = []
        
    if len(mhs)>0:
        colsj = ['Pengantar Sistem Digital','Organisasi Dan Arsitektur Komputer','Sistem Operasi',
                'Prak.Sistem Operasi','Komunikasi Data Dan Pengantar Jaringan','Jaringan Komputer',
                'Prak.Jaringan Komputer'] 

        kelj ={
            colsj[0] : [str(a.jaringans.Psd) for a in mhs],
            colsj[1] : [str(a.jaringans.Orkom) for a in mhs],
            colsj[2] : [str(a.jaringans.SistemOperasi) for a in mhs],
            colsj[3] : [str(a.jaringans.PrakSistemOperasi) for a in mhs],
            colsj[4] : [str(a.jaringans.Komdat) for a in mhs],
            colsj[5] : [str(a.jaringans.JaringanKomputer) for a in mhs],
            colsj[6] : [str(a.jaringans.PrakJaringanKomputer) for a in mhs],

        }
        dfj = pd.DataFrame(data=kelj)        
    else:
        dfj = []    
            
    if len(mhs)>0:
        colsr = ['Algoritma Dan Pemrograman','Prak.Algoritma Dan Pemrograman','Pengantar Teknologi Informasi',
                'Struktur Data','Sistem Basis Data','Prak.Sistem Basis Data','Pemrograman I','Prak.Pemrograman I',
                'Sistem Informasi','Pemrograman II','Prak.Pemrograman II','Analisa Dan Desain Perangkat Lunak','Artificial Intelligent']

        kelr ={            
            colsr[0] : [str(a.rpls.AlgoritmaDanPemrograman) for a in mhs],
            colsr[1] : [str(a.rpls.PrakAlgoritmaDanPemrograman) for a in mhs],
            colsr[2] : [str(a.rpls.PTI) for a in mhs],
            colsr[3] : [str(a.rpls.StrukturData) for a in mhs],
            colsr[4] : [str(a.rpls.SistemBasisData) for a in mhs],
            colsr[5] : [str(a.rpls.PrakSistemBasisData) for a in mhs],
            colsr[6] : [str(a.rpls.Pemrograman1) for a in mhs],
            colsr[7] : [str(a.rpls.PrakPemrograman1) for a in mhs],
            colsr[8] : [str(a.rpls.SistemInformasi) for a in mhs],
            colsr[9] : [str(a.rpls.Pemrograman2) for a in mhs],
            colsr[10] : [str(a.rpls.PrakPemrograman2) for a in mhs],
            colsr[11] : [str(a.rpls.Adpl) for a in mhs],
            colsr[12] : [str(a.rpls.ArtificialIntelligent) for a in mhs],
        }        
        dfr = pd.DataFrame(data=kelr)    
    else:
        dfr = []
        
    def ListTest(mhs):
        if len(mhs)>0:
            cols = ['Multimedia','Jaringan','Rpl']
            
            kel ={
                cols[0] : [str(a.tesdasars.NilaiMultimedia) for a in mhs],
                cols[1] : [str(a.tesdasars.NilaiJaringan) for a in mhs],
                cols[2] : [str(a.tesdasars.NilaiRPL) for a in mhs],
            }
            df = pd.DataFrame(data=kel)
            return df
        else:
            a = pd.DataFrame(columns=['Multimedia','Jaringan','Rpl'])
            return a
        
    def Mhsis(mhs):
        if len(mhs)>0:
            cols = ['nim','nama','jenis kelamin']
            
            kel ={
                cols[0] : [str(a.nim) for a in mhs],
                cols[1] : [str(a.nama) for a in mhs],
                cols[2] : [str(a.jenis_kelamin) for a in mhs],
            }
            df = pd.DataFrame(data=kel)
            return df
        else:
            return []

    mu = pd.DataFrame(data = ListTest(mhs).Multimedia)
    ja = pd.DataFrame(data = ListTest(mhs).Jaringan)
    rp = pd.DataFrame(data = ListTest(mhs).Rpl)

    def Hitung(a,b,c,d,e):
        tamp = []
        for x in range(len(mhs)):
            tampung = list()
            for z, i in enumerate(a):           
                total = e[z]
                if i is 'A':
                    tampung.append(4*total)
                elif i == 'B+': 
                    tampung.append(3.5*total)
                elif i is 'B':  
                    tampung.append(3*total)
                elif i == 'C+': 
                    tampung.append(2.5*total)
                elif i is 'C':  
                    tampung.append(2*total)
                elif i is 'D':
                    tampung.append(1.5*total)
                elif i is 'E':
                    tampung.append(1*total)
                else:
                    tampung.append(0)
                rata2 = sum(tampung)/d
                tmp = [round(rata2, 2), b]
                dframe = pd.DataFrame(data=tmp,columns=[c])
        tamp.append(dframe)
        return tamp

    def Mhultimedia(mul):
        Mhultimedia = []
        for i in range(len(mhs)):
            sks = [3,2,1]
            x = Hitung(dfm.loc[i],mu.loc[i][0],'Multimedia',6,sks)
            Mhultimedia.append(x)
        return Mhultimedia
        
    def Jharingan(jar):
        Jharingan = []
        for i in range(len(mhs)):
            sks = [3,3,2,1,4,2,1]
            x = Hitung(dfj.loc[i],ja.loc[i][0],'Jaringan',16,sks)
            Jharingan.append(x)
        return Jharingan

    def Rhpl(rpl):
        Rhpl = []
        for i in range(len(mhs)):
            sks = [2,1,3,3,2,1,1,2,2,1,2,4,3]
            x = Hitung(dfr.loc[i],rp.loc[i][0],'Rpl',27,sks)
            Rhpl.append(x)
        return Rhpl

    def tampungs(mhs):
        tampung1 = []
        for i in range(len(mhs)):
            mlt = Mhultimedia(mul)
            jrg = Jharingan(jar)
            lpr = Rhpl(rpl)
            gabungan = pd.concat([mlt[i][0],jrg[i][0],lpr[i][0]],axis=1)
            tampung1.append(gabungan)
        return tampung1

    tamps = tampungs(mhs)
    # def Total(mhs):
    #     t = []
    #     for i in range(len(mhs)):
    #         gabungan = pd.concat([Mhultimedia[i][0],Jharingan[i][0],Rhpl[i][0]],axis=1)
    #         t.append(gabungan)
    #     return t

    if len(mhs)>0:
        p1 = tamps[0].shape[1]
        p2 = tamps[0].shape[1]
        p3 = len(tamps[0].iloc[:,0])
    else:
        p1 = 3
        p2 = 3
        p3 = 2
    def IndexPr(mhs):
        arr0 = []
        hasil0 = []
        for y in range(len(mhs)):
            arr = []
            hasil = []
            for i in range(p1):
                arr1 = []
                hasil1 = []
                for j in range(p2):
                    arr2 = []
                    hasil2= []
                    for k in range(p3):
                        z = float(tamps[y].iloc[:,i][k])-float(tamps[y].iloc[:,j][k])
                        m = 0            
                        if (z <= 0):
                            m = 0
                        else:
                            m = 1
                        hasil2.append(z)
                        arr2.append(m)
                    arr1.append(arr2)
                    hasil1.append(hasil2)
                arr.append(arr1)
                hasil.append(hasil1)
            arr0.append(arr)
            hasil0.append(hasil)
            hasil1 = pd.DataFrame(arr0)
            hasil2 = pd.DataFrame(hasil0)
        return hasil1, hasil2

    def Tindex(mhs):
        has1 = IndexPr(mhs)[0]
        akhir = []
        for v in range(len(mhs)):
            akhir1 = []
            for i in range(len(tamps[v].iloc[0])):
                akhir2 = []
                for j in range(len(has1[i].loc[v])):
                    bla = sum(has1.loc[v].loc[i][j])*(1/len(has1.loc[v].iloc[i][j]))
                    akhir2.append(bla)
                akhir1.append(akhir2)
            akhir.append(akhir1)
        return akhir
    def Promethee1(mhs):
        promethee1 = []
        for m in range(len(mhs)):
            tmp1 = []
            for i in range(len(Tindex(mhs)[m])):
                tmp2 = []
                for j in range(len(Tindex(mhs)[m])):
                    tmp2.append(Tindex(mhs)[m][i][j])
                tmp1.append(tmp2)
            prometh = pd.DataFrame(data=tmp1, columns = ['A','B','C'], index = ['A', 'B', 'C'])
            promethee1.append(prometh)
        return promethee1

    prom1 = Promethee1(mhs)
    Lf = []
    for k in range(len(prom1)):
        lf1 = []
        for i in range(len(prom1[k])):
            jwb = (1/(len(prom1[k]) - 1)) * sum(prom1[k].iloc[i])
            lf1.append(jwb)        
        leaving = pd.DataFrame(data=lf1,columns=['Leaaving Flow'])
        Lf.append(leaving)

    Ef = []
    for k in range(len(prom1)):
        ef1 = []
        for i in range(len(prom1[k])):
            jwb = (1/(len(prom1[k])-1)) * sum(prom1[k].iloc[:,i])
            ef1.append(jwb)        
        entring = pd.DataFrame(data=ef1,columns=['Entring Flow'])
        Ef.append(entring)

    Nf = []
    for k in range(len(prom1)):
        nf1 = []
        for i in range(len(prom1[k])):
            jwb = Lf[k].iloc[i][0] - Ef[k].iloc[i][0]
            nf1.append(jwb)        
        net = pd.DataFrame(data=nf1,columns=['Net Flow'])
        Nf.append(net)

    def Nilai(mhs):
        if len(mhs)>0:
            nf = []
            gh = []
            rek = []
            alternative = ['MULTIMEDIA','JARINGAN','RPL']
            for k in range(len(prom1)):
                nf1 = []
                for i in range(len(prom1[k])):
                    jwb = Lf[k].iloc[i][0] - Ef[k].iloc[i][0]
                    nf1.append(jwb)     
                rek1 = []
                for x, y in enumerate(nf1):
                    if y == max(nf1):
                        rek1.append(alternative[x])                    
                    else:
                        continue
                rek.append('/'.join(rek1))
                gh.append(max(nf1))            
                net = pd.DataFrame(data=gh,columns=['Net Flow'])
                rekom = pd.DataFrame(data=rek,columns=['Rekomendasi'])            
                # a=Mhsis(mhs).index.get_values()
                hasil=pd.concat([Mhsis(mhs),rekom],axis=1)
            return hasil
        else:
            a = pd.DataFrame(columns=['Multimedia','Jaringan','Rpl'])
            return a

    # Nama Kolom
    alt = pd.DataFrame(['Multimedia','Jaringan','Rpl'],columns=['Rekomendasi'])

    Gabung = []
    for x in range(len(mhs)):
        z = pd.concat([Lf[x],Ef[x],Nf[x],alt],axis=1)
        Gabung.append(z)

    for k,v in enumerate(Gabung):
        Gabung[k].index.name=str(mhs[k])
    for k,v in enumerate(tamps):
        tamps[k].index.name=str(mhs[k])

    def Perangkingan(mhs):
        tt = Gabung
        if len(mhs)>0:
            rangking = []
            for x in range(len(Gabung)):
                rank = tt[x].sort_values(by='Net Flow', ascending=False)
                rangking.append(rank)
                
            return rangking
        else:
            a = pd.DataFrame(columns=['Multimedia','Jaringan','Rpl'])
            return a

    def Penggabungan(mhs):
        gab = []
        for x in range(len(mhs)):
            z = pd.concat([Lf[x],Ef[x],nf[x],alt],axis=1)
            gab.append(z)

        return gab

    multiD = []
    for k in range(len(prom1)):
        multiD.append(tamps[k].loc[0][0])
    Dmultimedia = pd.DataFrame(data=multiD,columns=['Multimedia'])

    jar = []
    for k in range(len(prom1)):
        jar.append(tamps[k].loc[0][1])
    Djaringan = pd.DataFrame(data=jar,columns=['Jaringan'])    

    rpl = []
    for k in range(len(prom1)):
        rpl.append(tamps[k].loc[0][2])
    Drpl = pd.DataFrame(data=rpl,columns=['RPL'])    

    def Msiswa(mhs):
        if len(mhs)>0:
            cols = ['nim','nama']
            
            kel ={
                cols[0] : [str(a.nim) for a in mhs],
                cols[1] : [str(a.nama) for a in mhs],
            }
            df = pd.DataFrame(data=kel)
            return df
        else:
            return []

    def Akademik(mhs):
        ms = Msiswa(mhs)
        if len(mhs)>0:
            a = pd.concat([ms,Dmultimedia,Djaringan,Drpl],axis=1)
            return a
        else:
            a = pd.DataFrame(columns=['Multimedia','Jaringan','Rpl'])
            return a

    multiT = []
    for k in range(len(prom1)):
        multiT.append(tamps[k].loc[1][0])
    Tmultimedia = pd.DataFrame(data=multiT,columns=['Multimedia'])



    jar = []
    for k in range(len(prom1)):
        jar.append(tamps[k].loc[1][1])
    Tjaringan = pd.DataFrame(data=jar,columns=['Jaringan'])    



    rpl = []
    for k in range(len(prom1)):
        rpl.append(tamps[k].loc[1][2])
    Trpl = pd.DataFrame(data=rpl,columns=['RPL'])    


    def TesDasar(mhs):
        if len(mhs)>0:        
            a = pd.concat([Msiswa(mhs),Tmultimedia,Tjaringan,Trpl],axis=1)
            return a
        else:
            a = pd.DataFrame(columns=['Multimedia','Jaringan','Rpl'])
            return a
            
    return Nilai(mhs), Akademik(mhs), TesDasar(mhs), Perangkingan(mhs), Orang(mhs)