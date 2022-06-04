
import imp
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


from .models import *
from .forms import  CreateUserForm
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login/')
def index(request):
    return render(request, 'main/index.html')

def kia(request):
    return render(request, 'main/kia.html')

def kiak5(request):
    return render(request, 'main/kiak5.html')

def seltos(request):
    return render(request, 'main/kiaseltos.html')
def hyundai(request):
    return render(request, 'main/hyundai.html')

def chevrolet(request):
    return render(request, 'main/chevrolet.html')

def news(request):
    return render(request, 'main/news.html')


def images(request):
    return render(request, 'main/images.html')


def contact(request):
    return render(request, 'main/contact.html')

def registerPage(request):
    
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

