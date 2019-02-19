from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$",views.LoginView.as_view(),name='login'),
    url(r'^proses/$', views.ProsesLoginView.as_view(),name='proses_login'),
    url(r'^logout/$', views.LogoutProsesView.as_view(),name='logout'),
	]
    