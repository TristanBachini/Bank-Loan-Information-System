from django.shortcuts import redirect, render
from loans_borrower.models import Loans
from .forms import *
from django.contrib import messages
from datetime import datetime

# Create your views here.


def viewLoanApps(request):
    user = request.user
    loans = Loans.objects.filter(user=user)
    
    data = {
        'loans' : loans,
    }
    return render(request, 'loans_borrower/view-loan-apps.html', data)


def viewLoanAppsInfo(request, pk):
    loan = Loans.objects.get(id=pk)

    data = {
        'loan' : loan,
    }
    return render(request, 'loans_borrower/view-loan-apps-info.html', data)   


def loanApply(request):
    today = datetime.now()
    loan_form = LoanApplyForm()
    if(request.method == "POST"):
        loan_form = LoanApplyForm(request.POST, request.FILES)
        if(loan_form.is_valid()):
            temp = loan_form.save(commit=False)
            temp.user = request.user
            temp.app_date = today
            print(request.POST)
            temp.save()
            messages.success(request, 'Application submitted.')
        else:
            messages.error(request, loan_form.errors)
    data = {
        'loan_form' : loan_form
    }
    return render(request, 'loans_borrower/loan-apply.html', data)


def loanDocsUpload(request,pk):
    loan = Loans.objects.get(id=pk)
    app_date = loan.app_date
    loan_form = LoanApplyForm(instance=loan)
    if(request.method == "POST"):
        loan_form = LoanApplyForm(request.POST, request.FILES, instance=loan)
        if(loan_form.is_valid()):
            temp = loan_form.save(commit=False)
            temp.app_date = app_date
            temp.user = request.user
            print(request.POST)
            temp.save()
            messages.success(request, 'Loan Documents Uploaded.')
        else:
            messages.error(request, loan_form.errors)
    data = {
        'loan_form' : loan_form
    }
    return render(request, 'loans_borrower/loan-docs-upload.html', data)