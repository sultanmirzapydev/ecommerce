from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
	fullname  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'your full name'}))
	email     = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your email'}))
	content   = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'your content'}))

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not "gmail.com" in email:
			raise forms.ValidationError('email has to be gmail.com')
		return email

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	username = forms.CharField()
	email    = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2= forms.CharField(label= 'confirm password', widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		check    = User.objects.filter(username=username)
		if check.exists():
			raise forms.ValidationError('username is taken, use new username')
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs    = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('email is already taken')
		return email



	def clean(self):
		data = self.cleaned_data
		password = data.get('password')
		password2 = data.get('password2')
		if password2 != password:
			raise forms.ValidationError('password must match')
		return data