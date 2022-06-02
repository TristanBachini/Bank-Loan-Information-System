global bankBal

from django.shortcuts import render,redirect
from decimal import Decimal
from create_manage_acc.models import BankAccount
from . import views
from create_manage_acc.forms import AccountRegForm, BankAccountForm
from django.contrib.auth.models import Group
from loans_borrower.models import Loans
import datetime
from django.db.models.functions import ExtractMonth, ExtractYear
from bank_calculator.views import pmt

# Create your views here.
def account_registration(request):
    user = request.user
    loans = Loans.objects.filter(user=user)
    
    group = Group.objects.get(name='hasbankaccount')
    
    if(request.method == 'POST'):
        form = AccountRegForm()
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
        print(form.errors)
        if form.is_valid():
            bankBal = request.session.get('bankBal')
            if bankBal is None:
                bankBal = 0
            request.session['bankBal'] = bankBal
            user.groups.add(group)
            print("valid form")
            form.save()
            print(bankBal)
            return redirect('/create-manage-account/deposit-money' ,{'bankBal': bankBal})
    form = AccountRegForm()
    return render(request, 'create_manage_acc/create-acc.html', {'form':form})

def deposit_money(request):
    if not BankAccount.objects.filter(user = request.user).exists():
        print("does not exist")
        form = BankAccountForm()
        if(request.method == 'POST'):
            if request.POST.get('balance') is None:
                
                form = BankAccountForm({
                    'user':request.user,
                    'deposit': request.POST.get('deposit'),
                    'balance': 0
                    })
            if form.is_valid():
                form.save()
                return render(request, 'create_manage_acc/deposit-money.html', {'form':form})
        return render(request, 'create_manage_acc/deposit-money.html', {'form':form})
    print("daan")          
    bank_acc = BankAccount.objects.filter(user = request.user).latest('id')
    bankBal = bank_acc.balance
    if bankBal is None:
        bankBal = 0
    form = BankAccountForm()
    if(request.method == 'POST'):
        #bankBal = request.session.get('bankBal')
        bankBal = float(request.POST.get('deposit')) + float(bankBal)
        form = BankAccountForm({
            'user':request.user,
            'deposit': request.POST.get('deposit'),
            'balance': bankBal
            })
        if form.is_valid():
            today = datetime.datetime.now()
            post  = form.save(commit = False)
            for loan in Loans.objects.filter(user = request.user, status="Approved"):
                print(loan.app_date.strftime("%m %d"))
                print(today.strftime("%m %d"))
                if(loan.app_date.strftime("%m %d") == today.strftime("%m %d")):
                        due = True
                        num_of_months = float(loan.no_of_payments)
                        loan_amt = float(loan.loan_amt)
                        loan_bal = float(loan.loan_bal)
                        percentage = 0.0525
                        monthly_pmt = pmt(percentage, loan_amt, num_of_months)
                        print("Monthly PMT")
                        print(monthly_pmt)
                        print("loan balance: ")
                        print(loan_bal)
                        # print(bankBal)
                        bankBal -= monthly_pmt
                        loan_bal -= monthly_pmt
                        loan.loan_bal = "{:.2f}".format(loan_bal)
                        if bankBal < monthly_pmt:
                            BankAccount.objects.filter(user=request.user).delete()
                            print("Bank account deleted")
                            user = request.user
                            group = Group.objects.get(name='hasbankaccount') 
                            user.groups.remove(group)
                            loan.loan_tag = "Delinquent"
                            return render(request, 'bank_calculator/loancalculator.html')
                        if(loan.loan_bal <= 0):
                            loan.loan_tag = "Completed"
                        loan.save()
                        print("new loan bal:")
                        print(loan.loan_bal)
                        print(bankBal)
            post.balance = "{:.2f}".format(bankBal)
            #print(form.balance)
            post.save()
            form = BankAccountForm({
            'user':request.user,
            'deposit': request.POST.get('deposit'),
            'balance': post.balance
            })
            return render(request, 'create_manage_acc/deposit-money.html', {'form':form})

    form = BankAccountForm()
    return render(request, 'create_manage_acc/deposit-money.html', {'form':form})
