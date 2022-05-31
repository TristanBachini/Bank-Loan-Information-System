global bankBal

from django.shortcuts import render,redirect

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
            bankBal = request.session.get('bankBal')
            if bankBal is None:
                bankBal = 0
            request.session['bankBal'] = bankBal
            user.groups.add(group)
            form.save()
            print(bankBal)
            return redirect('/create-manage-account/deposit-money' ,{'bankBal': bankBal})
    form = AccountRegForm()
    return render(request, 'create_manage_acc/create-acc.html', {'form':form})

def deposit_money(request):
    if(request.method == 'POST'):
        bankBal = request.session.get('bankBal')
        #print(bankBal)
        bankBal = int(request.POST.get('deposit')) + int(bankBal)
        request.session['bankBal'] = bankBal
        print(bankBal)
        form = BankAccountForm({
                'user':request.user,
                'deposit': request.POST.get('deposit'),
                'balance': bankBal})
        form.user = request.user
        print(form.errors)
        if form.is_valid():
            form.save()
            form = BankAccountForm({
                'balance': bankBal})
            return render(request, 'create_manage_acc/deposit-money.html', {'form':form})
    form = BankAccountForm()
    return render(request, 'create_manage_acc/deposit-money.html', {'form':form})