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
    # for loan in loans:
    #     if loan.status == "Approved":
            
    group = Group.objects.get(name='hasbankaccount')
    
    if(request.method == 'POST'):
        form = AccountRegForm(request.POST)
        if form.is_valid():
            bankBal = 0
            user.groups.add(group)
            form.user = request.user
            form.save()
            return render(request, 'create_manage_acc/deposit-money.html', {'loans':loans})
    form = AccountRegForm()
    return render(request, 'create_manage_acc/create-acc.html', {'form':form})

def deposit_money(request):
    # print (request.user)
    # #form = BankAccountForm()
    # if(request.method == 'POST'):
    #     form = BankAccountForm({
    #             'user':request.user,
    #             'balance': request.POST.get('balance')})
    #     print (form.errors)
    #     #print(form)
    #     if form.is_valid():
    #         print("Valid form")
    #         # form = BankAccountForm({
    #         #         'user':request.user,
    #         #         'balance': request.POST.get('balance')})
            
    #         form.save()
    #         return render(request, 'create_manage_acc/deposit-money.html', {'form':form})
    # #user = BankAccount.objects.get(user=request.user)
    # # if user.balance == 0:
    # #     if(request.method == 'POST'):
    # #         form = BankAccountForm(instance = user)
    # #         if form.is_valid():
    # #             form.user_id = request.user
    # #             form.save()
    # #             bankBal = request.POST.get('balance')
    # #         return render(request, 'create_manage_acc/deposit-money.html', {'form':form})       
    # # else:
    # #     if(request.method == 'POST'):
    # #         bankBal += request.POST.get('balance')
    # #         form = BankAccountForm({'user':user, 'balance':request.POST.get('balance')})
    # #         return render(request, 'create_manage_acc/deposit-money.html', {'form':form})           
    # form = BankAccountForm()
    # return render(request, 'create_manage_acc/deposit-money.html', {'form':form})

    print (request.user)
    #user = BankAccount.objects.get(user=request.user)
    # if user.balance == 0:
    #     if(request.method == 'POST'):
    #         form = BankAccountForm(instance = user)
    #         if form.is_valid():
    #             form.user_id = request.user
    #             form.save()
    #             bankBal = request.POST.get('balance')
    #         return render(request, 'create_manage_acc/deposit-money.html', {'form':form})       
    # else:
    #     if(request.method == 'POST'):
    #         bankBal += request.POST.get('balance')
    #         form = BankAccountForm({'user':user, 'balance':request.POST.get('balance')})
    #         return render(request, 'create_manage_acc/deposit-money.html', {'form':form})           
  
    form = BankAccountForm()
    if(request.method == 'POST'):
        form = BankAccountForm({
                'user':request.user,
                'balance': request.POST.get('balance')})
        #print(form.user)
        print(form.errors)

    return render(request, 'create_manage_acc/deposit-money.html', {'form':form})