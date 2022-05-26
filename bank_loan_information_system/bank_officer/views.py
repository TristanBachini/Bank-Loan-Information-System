from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def dashboard (request):
    return render(request, 'bank_officer/dashboard.html')

def review (request):
    return render(request, 'bank_officer/review.html')

def approved (request):
    return render(request, 'bank_officer/approved.html')

def rejected (request):
    return render(request, 'bank_officer/rejected.html')


def logout_page(request):
    logout(request)
    print("it worked until here tho")
    return render(request, "main/home.html")