from django.shortcuts import render
from loans_borrower.models import Loans
from .forms import *

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
    loan_form = LoanApplyForm()

    data = {
        'loan_form' : loan_form
    }
    return render(request, 'loans_borrower/loan-apply.html', data)