from django.shortcuts import render, redirect
from .models import Room
from .models import Product
from .models import Shema
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):

    room = Room.objects.all()
    product = Product.objects.all()
    context = {'room':room, 'product':product}
    return render(request, 'app/home.html', context)

def support(request):
    context = {}
    return render(request,'app/support.html')

# def (request):
#     context = {}
#     return render(request,'app/support.html')

def about(request):
    return render(request,'app/about.html')
def contact(request):
    return render(request, 'app/contact.html')
def services(request):
    return render(request, 'app/services.html')
def apply(request):
    return render(request,'app/apply.html')

