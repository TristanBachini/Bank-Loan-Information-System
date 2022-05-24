from django.shortcuts import render

from bank_calculator.models import Months_To_Pay

# Create your views here.
def loan_compute(percentage,selling_price,amount,number_of_months):
    

    
    return monthly_payment

def loan_calculator(request):
    months = Months_To_Pay.objects.all()

    if(request.method == 'POST'):
        percentage=request.POST.get('percentage')
        selling_price=request.POST.get('sellingprice')
        amount=request.POST.get('amount')
        number_of_months=request.POST.get('months')
        preffered_unit=request.POST.get('unit')

        if(percentage or selling_price or amount or number_of_months or preffered_unit is None):
            monthly_payment = loan_compute(percentage,selling_price,amount,number_of_months)
            monthly_payment = (selling_price/number_of_months) + (selling_price/number_of_months)*.20
            data = {'monthly_payment':monthly_payment,'months':number_of_months}

    return render(request, 'bank_calculator/loancalculator.html',{'months':months})