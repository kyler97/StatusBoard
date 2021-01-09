from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name' ,'last_name')
	def __init__(self, *args, **kwargs):
		super(EditProfileForm, self). __init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):
	email = forms.EmailField( widget= forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self). __init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'


	
class addunitform(forms.ModelForm):
	class Meta:
		model = unit
		fields = [
			'picture',
			'unit_no',
			'Status',
			'Problem',
			'Notified',
			'Date',
			'Location',

		]

class editunitform(forms.ModelForm):
	class Meta:
		model = unit
		fields = [
			'Status',
			'Problem',
			'Notified',
			'Date',
			'Location',

		]

class addeventform(forms.ModelForm):
	class Meta:
		model = courses
		fields = [
			'Title',
			'Desription',
			'Instructor',
			'Location',
			'Date',
		]
		