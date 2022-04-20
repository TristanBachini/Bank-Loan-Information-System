from django.shortcuts import render

from bank_calculator.models import Months_To_Pay

# Create your views here.

def loan_calculator(request):
    months = Months_To_Pay.objects.all()
    if(request.method == 'POST'):
        print("Im gay")
    return render(request, 'bank_calculator/loancalculator.html',{'months':months})