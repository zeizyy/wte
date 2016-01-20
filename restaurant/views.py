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

def init(request):
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
	userprofile.base = array
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
	return render_to_response('restaurant/next.html',\
		{'next':tup[0]})


def get_array(request):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('Login'))
	userprofile = UserProfile.objects.get(user = user)
	array = userprofile.array
	return HttpResponse(array)

def add_restaurant(request):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('Login'))
	userprofile = UserProfile.objects.get(user = user)
	if request.method == 'POST':
		name = request.POST['name']
		if name:
			r = Restaurant(name = name)
			try:
				r.save()
			except:
				return HttpResponseRedirect(reverse('addRestaurant'))
			r.user.add(user)
			base = userprofile.base
			array = userprofile.array
			base = json.loads(base)
			array = json.loads(array)
			base = add_arr(base, name)
			array = add_arr(array, name)
			userprofile.base = base
			userprofile.array = array
			userprofile.save()
			return HttpResponseRedirect(reverse('viewAll'))
	return render_to_response('restaurant/add.html')

def add_arr(array, name):
	l = len(array)
	array.append([name, 1.0/l])
	s = sum(tup[1] for tup in array)
	for tup in array:
		tup[1] = tup[1]/s
	array_str = json.dumps(array)
	return array_str

def avg_arr(array, index):
	l = len(array)
	distr = array[index][1]/(l-1)
	for i in range(l):
		if i == index:
			array[i][1] = 0
		else:
			array[i][1] += distr
	return distr

def delete_restaurant(request, restaurant_id):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('Login'))
	userprofile = UserProfile.objects.get(user = user)
	r = Restaurant.objects.get(pk = restaurant_id)
	name = r.name
	r.user.remove(user)
	array = json.loads(userprofile.array)
	base = json.loads(userprofile.base)
	array = delete_arr(array, name)
	base = delete_arr(base, name)
	userprofile.array = array
	userprofile.base = base
	userprofile.save()
	return HttpResponseRedirect(reverse('viewAll'))

def delete_arr(array, name):
	index = -1
	distr = -1
	l = len(array)
	for i in range(l):
		if array[i][0] == name:
			index = i
			distr = array[i][1]
			break
	del array[index]
	s = 1 - distr
	for tup in array:
		tup[1] = tup[1]/s
	array_str = json.dumps(array)
	return array_str

