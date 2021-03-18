from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, User
from django.http import HttpResponse
from bins.forms import BinForm
from bins.models import Binss
from django.contrib.auth.models import User
from django.contrib import messages

def home_page(*args, **kwargs):
	return HttpResponse('<h1>salut</h1>')

def login_page(request, *args, **kwargs):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
	return render(request, 'login.html', {})

def registration_page(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'registration.html', {'form':form})

def bins_page(request):
	form = BinForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit = False)
		obj.user = request.user
		obj.save()
		messages.success(request, 'Your bin has been saved.')
	form = BinForm(request.POST or None)
	return render(request, 'binsHome.html', {'form':form})

def your_bins(request):
	current_user = request.user
	fields = Binss.objects.all()
	context = {'object': fields}
	return render(request, 'yourBins.html',context)
