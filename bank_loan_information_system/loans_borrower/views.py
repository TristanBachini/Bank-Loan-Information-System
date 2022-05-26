from django.shortcuts import render
from loans_borrower.models import Loans

# Create your views here.


def viewLoanApps(request):
    loans = Loans.objects.all()

    data = {
        'loans' : loans,
    }

    return render(request, 'loans_borrower/viewLoanApps.html', data)    