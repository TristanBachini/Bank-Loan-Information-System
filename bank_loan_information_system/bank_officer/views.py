from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render
from loans_borrower.models import Loans
from loans_borrower.forms import *

# Create your views here.
def dashboard (request):
    review = Loans.objects.filter(status='For Review').count()
    approved = Loans.objects.filter(status='Approved').count()
    rejected = Loans.objects.filter(status='Rejected').count()
    data = {
        'review':review, 'approved':approved, 'rejected':rejected
    }
    return render(request, 'bank_officer/dashboard.html', data)

def review (request):
    loans = Loans.objects.filter(status='For Review')
    data = {
        'loans' : loans,
    }
    return render(request, 'bank_officer/review.html', data)

def approved (request):
    loans = Loans.objects.filter(status='Approved')
    data = {
        'loans' : loans,
    }
    return render(request, 'bank_officer/approved.html', data)

def rejected (request):
    loans = Loans.objects.filter(status='Rejected')
    data = {
        'loans' : loans,
    }
    return render(request, 'bank_officer/rejected.html', data)

def view_loan_app(request,pk):
    loan = Loans.objects.get(id=pk)
    data = {
        'loan' : loan,
    }
    return render(request, 'bank_officer/loan-app.html', data) 

def logout_page(request):
    logout(request)
    print("it worked until here tho")
    return render(request, "main/home.html")