from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import permission_required,login_required
from management.login.forms import AuthenticateForm

class LoginView(View):
	def get(self,request):
		template = 'login/login.html'
		data = {
		'template' : template
		}
		return render(request,template,data)

class ProsesLoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password ) 
        if user:            
            login(request, user)            
            return redirect('mahasiswa:home')
        messages.warning(request, 'Username or Password Incorrect !')
        return redirect('/') 
		

class LogoutProsesView(View):
    def get(self, request):
        if request.user.is_authenticated():
            logout(request)
            return redirect('login')