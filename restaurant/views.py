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

import json
import random
# Create your views here.

def viewAll(request):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('Login'))
	restaurant = Restaurant.objects.filter(user = user)
	return render_to_response('restaurant/all.html',\
		{'restaurant':restaurant})

def calc(request):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('Login'))
	userprofile = UserProfile.objects.get(user = user)
	restaurant = Restaurant.objects.filter(user=user)
	size = len(restaurant)
	l1 = [r.name for r in restaurant]
	l2 = [1.0/size]*size
	array = json.dumps(list(zip(l1, l2)))
	userprofile.array = array
	userprofile.save()
	return HttpResponseRedirect(reverse('viewAll'))

def get_next(request):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('Login'))
	userprofile = UserProfile.objects.get(user = user)
	array = userprofile.array
	array = json.loads(array)
	r = random.random()
	index = 0
	while r > 0:
		tup = array[index]
		r -= tup[1]
		index += 1
	index -= 1
	tup = array[index]
	avg_arr(array, index)
	array = json.dumps(array)
	userprofile.array = array
	userprofile.save()
	return HttpResponse(tup[0]+" "+str(r))

def get_array(request):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('Login'))
	userprofile = UserProfile.objects.get(user = user)
	array = userprofile.array
	return HttpResponse(array)

def add_restaurant(request):
	return render_to_response('restaurant/add.html')

def avg_arr(array, index):
	l = len(array)
	distr = array[index][1]/(l-1)
	for i in range(l):
		if i == index:
			array[i][1] = 0
		else:
			array[i][1] += distr
	return distr