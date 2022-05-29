from django.shortcuts import render
from . import views
from .forms import AccountRegForm
from django.contrib.auth.models import Group

# Create your views here.
def account_registration(request):
    group = Group.objects.get(name='hasbankaccount')
    user = request.user
    if(request.method == 'POST'):
        form = AccountRegForm(request.POST)
        if form.is_valid():
            user.groups.add(group)
            #form.save()
            return render(request, 'create_manage_acc/deposit-money.html')
    form = AccountRegForm()
    return render(request, 'create_manage_acc/create-acc.html', {'form':form})

def deposit_money(request):

    return render(request, 'create_manage_acc/deposit-money.html')