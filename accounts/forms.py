from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=200,help_text='Required')
	Name = forms.CharField(max_length=100,label="NAME")
	Age = forms.IntegerField()
	Gender = forms.CharField()

	class Meta:
		model = User
		fields = ('username','email','Name','Age','Gender','password1','password2')