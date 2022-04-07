from django.shortcuts import render, redirect
from django.urls import reverse
from login_app.forms import UserForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_page(request):
    #if a form has been submitted in login page, it will be authenticated.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        #check if user credentials is registered. If not, it will return to login page with error message
        if user is not None:
            login(request, user)
            return render(request, "main/home.html")
        else:
            messages.info(request, "Username or Password is incorrect.")
            return render(request, "login_app/login.html")

    return render(request, "login_app/login.html")


def register(request):
    form = UserForm()
    data = {"form":form}
    if(request.method=='POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            borrower = Group.objects.get(name='borrower')
            borrower.user_set.add(User.objects.get(username = form.cleaned_data.get('username')).id)            
            return render(request, "login_app/login.html")
        else:
            data = {"form":form}
            return render(request, "login_app/register.html",data)
    return render(request, "login_app/register.html",data)