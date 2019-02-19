from django import forms
from django.contrib.auth.models import User

class AuthenticateForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)

	class Meta:
		model = User