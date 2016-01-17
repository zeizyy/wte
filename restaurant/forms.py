#coding=utf-8 
from django import forms
from restaurant.models import UserProfile, Restaurant
from django.forms import EmailInput,Textarea, NumberInput, DateTimeInput, ModelMultipleChoiceField,CheckboxInput, TextInput, PasswordInput
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']