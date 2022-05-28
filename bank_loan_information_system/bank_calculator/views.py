from calendar import month
from django.shortcuts import render
from bank_calculator.models import Months_To_Pay

# Create your views here.
def pmt(percentage, loan, number_of_months):

    number_of_months = int(number_of_months)
    #interest rate is 5.25%
    #formula for pmt used in spreadsheet
    monthly_payment = (loan*(0.0525/12))/(1-(1+(0.0525/12))**-(12*(number_of_months/12)))

    return monthly_payment

def loan_compute(percentage,amount,preferred_unit,selling_price,loan,number_of_months,months):

    monthly_payment = pmt(percentage,loan,number_of_months)

    selling_price = "{:.2f}".format(float(selling_price))
    amount = "{:.2f}".format(float(amount))
    percentage = "{:.2f}".format(float(percentage))
    loan = "{:.2f}".format(float(loan))
    monthly_payment = "{:.2f}".format(float(monthly_payment))

    summary  = {'number_of_months':number_of_months,'percentage':percentage,'payment':monthly_payment,
    'amount':amount,'unit':preferred_unit,'price':selling_price,'loan':loan,'months':months}
    
    return summary

def loan_calculator(request):
    months = Months_To_Pay.objects.all()
    
    if(request.method == 'POST'):

        percentage=request.POST.get('percentage')
        selling_price=request.POST.get('sellingprice')
        amount=request.POST.get('amount')
        number_of_months=request.POST.get('months')
        preffered_unit=request.POST.get('unit')
        amount_financed = float(selling_price) - float(amount)

        data = loan_compute(percentage,amount,preffered_unit,selling_price,amount_financed,number_of_months,months)

        return render(request, 'bank_calculator/loancalculator.html',data)

    return render(request, 'bank_calculator/loancalculator.html',{'months':months})