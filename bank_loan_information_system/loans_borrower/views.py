from django.shortcuts import render
from loans_borrower.models import Loans
from .forms import *
from django.contrib import messages

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
    user = request.user
    loan_form = LoanApplyForm(initial={'user': user})
    if(request.method == "POST"):
        loan_form = LoanApplyForm(request.POST)

        if(loan_form.is_valid()):
            loan_form.save()
            messages.success(request, 'Application submitted.')
        else:
            messages.error(request, loan_form.errors)
    data = {
        'loan_form' : loan_form
    }
    return render(request, 'loans_borrower/loan-apply.html', data)