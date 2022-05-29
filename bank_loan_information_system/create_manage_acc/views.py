from django.shortcuts import render
from . import views
from .forms import AccountRegForm
from django.contrib.auth.models import Group
from loans_borrower.models import Loans

# Create your views here.
def account_registration(request):
    user = request.user
    loans = Loans.objects.filter(user=user)
    # for loan in loans:
    #     if loan.status == "Approved":
            
    group = Group.objects.get(name='hasbankaccount')
    
    if(request.method == 'POST'):
        form = AccountRegForm(request.POST)
        if form.is_valid():
            user.groups.add(group)
            #form.save()
            return render(request, 'create_manage_acc/deposit-money.html', {'loans':loans})
    form = AccountRegForm()
    return render(request, 'create_manage_acc/create-acc.html', {'form':form})

def deposit_money(request):

    return render(request, 'create_manage_acc/deposit-money.html')