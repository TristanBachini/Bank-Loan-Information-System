global bankBal

import re
from django.shortcuts import render

from create_manage_acc.models import BankAccount
from . import views
from create_manage_acc.forms import AccountRegForm, BankAccountForm
from django.contrib.auth.models import Group
from loans_borrower.models import Loans

# Create your views here.
def account_registration(request):
    user = request.user
    loans = Loans.objects.filter(user=user)
    
    group = Group.objects.get(name='hasbankaccount')
    
    if(request.method == 'POST'):
        form = AccountRegForm(
            {
                'user': request.user,
                'first_name': request.POST.get('first_name'),
                'last_name' : request.POST.get('last_name'),
                'sex': request.POST.get('sex'),
                'marital_status' : request.POST.get('marital_status'),
                'email': request.POST.get('email'),
                'prefix': request.POST.get('prefix'),
                'address': request.POST.get('address'),
                'phone': request.POST.get('phone')    
            })
        form.user = request.user
        if form.is_valid():
            user.groups.add(group)
            form.save()
            return render(request, 'create_manage_acc/deposit-money.html', {'loans':loans})
    form = AccountRegForm()
    return render(request, 'create_manage_acc/create-acc.html', {'form':form})

def deposit_money(request):
    if(request.method == 'POST'):
        form = BankAccountForm({
                'user':request.user,
                'deposit': request.POST.get('deposit')})
        #print(form.user)
        #form = BankAccountForm(request.POST)
        form.user = request.user
        print(form.errors)
        if form.is_valid():
            print("valid form")
            form.save()
            return render(request, 'create_manage_acc/deposit-money.html', {'form':form})
    form = BankAccountForm()
    return render(request, 'create_manage_acc/deposit-money.html', {'form':form})