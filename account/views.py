#coding=utf-8 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from restaurant.models import Restaurant, UserProfile
from restaurant.forms import LoginForm
#csrf exempt
from django.views.decorators.csrf import csrf_exempt

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import restaurant

# Create your views here.
def login_user(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, \
			password=password)
		if user is not None and user.is_active:
			login(request, user)
			return HttpResponseRedirect(reverse('viewAll'))
	login_form = LoginForm()
	return render_to_response('restaurant/login.html',\
		{'login_form':login_form})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('Login'))

def register_user(request):
	if request.method == 'POST':
		user_form = LoginForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			userprofile = UserProfile(user = user)
			userprofile.save()
			return HttpResponseRedirect(reverse('Login'))
	loginForm = LoginForm()
	return render_to_response('account/register.html', \
		{'loginForm':LoginForm})