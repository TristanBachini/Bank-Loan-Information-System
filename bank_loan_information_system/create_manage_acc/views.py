from django.shortcuts import render
from . import views
from .forms import AccountRegForm

# Create your views here.
def account_registration(request):
    # if(request.method == 'POST'):

    #     return render(request, 'create_manage_acc/create-acc.html')
    form = AccountRegForm()
    return render(request, 'create_manage_acc/create-acc.html', {'form':form})