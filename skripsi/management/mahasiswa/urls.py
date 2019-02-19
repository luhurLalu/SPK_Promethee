from django.conf.urls import url
from management.mahasiswa import views
 
urlpatterns = [
    url (r'^$', views.HomeView.as_view(), name='home'),
    url (r'^mahasiswa/$', views.ListMahasiswaView.as_view(), name='mahasiswa'),
    url (r'^data-rekomendasi$', views.ListHasilRekomendasiMahasiswa.as_view(), name='data_rekomendasi'),    
    # url (r'^detail_mahasiswa', views.ListDetailMahasiswa.as_view(), name='detail_mahasiswa'),    
    url (r'^add_data$',views.TambahDataView.as_view(),name='add_data'),
    # url (r'update$',views.UpdateView.as_view(),name='update'),
    url (r'^view_data/(?P<id>\d+)$',views.ViewDataView.as_view(),name='view_data'),
    # url (r'^read_data/(?P<id>\d+)$',views.ReadDataView.as_view(),name='read_data'),    


    url(r'^delete/(?P<idMhs>\d+)/$',views.HapusView.as_view(),name='delete'),

    url (r'^edit-data/(?P<id>\d+)$', views.EditView.as_view(), name='edit_data'),
    url (r'^update-data/(?P<id>\d+)$', views.UpdateView.as_view(), name='update_data'),
    url (r'^detail-promethee/(?P<id>\d+)$', views.ListDetailMahasiswa.as_view(), name='detail'),

    url (r'^kriteria-akademik', views.ListAkademikMahasiswa.as_view(), name='kriteria_akademik'),
    url (r'^kriteria-test', views.ListTestMahasiswa.as_view(), name='kriteria_test'),    
]