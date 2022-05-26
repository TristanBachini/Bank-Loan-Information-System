from django.shortcuts import render

# Create your views here.
def dashboard (request):
    return render(request, 'bank_officer/dashboard.html')

def review (request):
    return render(request, 'bank_officer/review.html')

def approved (request):
    return render(request, 'bank_officer/approved.html')

def rejected (request):
    return render(request, 'bank_officer/rejected.html')
