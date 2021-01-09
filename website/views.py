from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from .forms import *
from .models import *
from django.http import HttpResponseRedirect

def home(request):
	return render(request,'signtemplates/home.html', {} )

def login_user(request):
	if request.method =='POST':
		username = request.POST['Username']
		password = request.POST['Password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You are logged in'))
			return redirect('home')
		else:
			messages.success(request, ('Invaild login'))
			return redirect('login')


	else:
		return render(request,'signtemplates/login.html', {} )

def logout_user(request):
	logout(request)
	messages.success(request, ('Logged out'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, ('You are Registered'))
			return redirect('home')

	else:
		form = SignUpForm()
	context = {'form' : form}	
	return render(request,'signtemplates/register.html', context )

def profile(request):
	return render(request,'signtemplates/profile.html', {} )


def unitBoard(request):
	all_items = unit.objects.all()
	return render(request, 'signtemplates/unitBoard.html', {'all_items' : all_items})

def station1(request):
	all_items = unit.objects.filter(Location="Station 1")
	return render(request, 'signtemplates/station1.html', {'all_items' : all_items})

def st2(request):
	all_items = unit.objects.filter(Location="Station 2")
	return render(request, 'signtemplates/st2.html', {'all_items' : all_items})
def st3(request):
	all_items = unit.objects.filter(Location="Station 3")
	return render(request, 'signtemplates/st3.html', {'all_items' : all_items})
def st4(request):
	all_items = unit.objects.filter(Location="Station 4")
	return render(request, 'signtemplates/st3.html', {'all_items' : all_items})


def outofservice(request, list_id):
	item = unit.objects.get(pk=list_id)
	item.Status = False
	item.save()
	return redirect('unitBoard')

def inservice(request, list_id):
	item = unit.objects.get(pk=list_id)
	item.Status = True
	item.save()
	return redirect('unitBoard')
def st1(request):
	return render(request, 'signtemplates/st1.html', {})

def weather(request):
	import json
	import requests



	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+ zipcode +'&distance=5&API_KEY=5D6254D7-9600-491A-861A-3A8E8F41647F')
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = 'error'


		if api[1]['Category']['Name'] == "Good" :
			cat_desription= '(0-50) Air Quality is considered satisfactory, and air pollution poses little or no risk.'
			cat_color = 'good'
		elif api[1]['Category']['Name'] == "Moderate": 
			cat_desription = '(51-100) If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors.'
			cat_color = 'moderate '
		elif api[1]['Category']['Name']== "Unhealthy for Sensitve Groups": 
			cat_desription = '(101-150) People with lung disease are at risk for health effects.'
			cat_color = 'usg'
		elif api[1]['Category']['Name'] == "Unhealthy":
			cat_desription = '(151-200) Everyone may experience health effects, members of sensitve groups may experience more serious health effects.'
			cat_color = 'unhealthy'
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			cat_desription ='(201-300) Health alert: everyone may experience more serious health effects.'
			cat_color = 'veryunhealthy'
		elif api[1]['Category']['Name'] == "Hazardous" :
			cat_desription = '(301-500) Health warnings of emergency conditions. The entire population is more likely to be effected.'
			cat_color = 'hazardous'



		return render(request, 'signtemplates/weather.html', 
			{'api' : api, 
			'cat_desription': cat_desription, 
			'cat_color' : cat_color,})


	else:

		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=37890&distance=5&API_KEY=5D6254D7-9600-491A-861A-3A8E8F41647F')
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = 'error'


		if api[1]['Category']['Name'] == "Good" :
			cat_desription= '(0-50) Air Quality is considered satisfactory, and air pollution poses little or no risk.'
			cat_color = 'good'
		elif api[1]['Category']['Name'] == "Moderate": 
			cat_desription = '(51-100) If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors.'
			cat_color = 'moderate '
		elif api[1]['Category']['Name']== "Unhealthy for Sensitve Groups": 
			cat_desription = '(101-150) People with lung disease are at risk for health effects.'
			cat_color = 'usg'
		elif api[1]['Category']['Name'] == "Unhealthy":
			cat_desription = '(151-200) Everyone may experience health effects, members of sensitve groups may experience more serious health effects.'
			cat_color = 'unhealthy'
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			cat_desription ='(201-300) Health alert: everyone may experience more serious health effects.'
			cat_color = 'veryunhealthy'
		elif api[1]['Category']['Name'] == "Hazardous" :
			cat_desription = '(301-500) Health warnings of emergency conditions. The entire population is more likely to be effected.'
			cat_color = 'hazardous'



		return render(request, 'signtemplates/weather.html', 
			{'api' : api, 
			'cat_desription': cat_desription, 
			'cat_color' : cat_color,})
def addunit(request):
	form = addunitform(request.POST)
	
	if request.method == 'POST':
		form = addunitform(request.POST)
		if form.is_valid():
			messages.success(request, ('Unit added'))
			form.save()


	return render(request, 'signtemplates/addunit.html', {'form': form})
def allunits(request):
	items = unit.objects.all()
	return render(request, 'signtemplates/allunits.html', {'items' : items})

def editunit(request,pk):
	truck = unit.objects.get(id=pk)
	form = editunitform(instance=truck)

	if request.method == 'POST':
		form = editunitform(request.POST, instance=truck)
		if form.is_valid():
			form.save()
			messages.success(request, ('Unit Updated'))
			return redirect('unitBoard')
	context = {'form' : form, 'truck' : truck}
	return render(request, 'signtemplates/addunit.html', context)

def delete(request, list_id):
	truck = unit.objects.get(pk=list_id)
	truck.delete()
	messages.success(request, ('Unit Removed'))
	return redirect('unitBoard')
def calendar(request):
	event = courses.objects.all()
	return render(request, 'caltemp/calendar.html',{'event' : event})
	
