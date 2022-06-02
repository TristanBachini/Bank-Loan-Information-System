from django.shortcuts import render, redirect
from django.contrib.auth import logout
from loans_borrower.models import Loans
from loans_borrower.forms import *
# for generating pdf
from io import BytesIO
from django.template.loader import get_template
import os
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def dashboard (request):
    review = Loans.objects.filter(status='For Review').count()
    approved = Loans.objects.filter(status='Approved').count()
    rejected = Loans.objects.filter(status='Rejected').count()
    data = {
        'review':review, 'approved':approved, 'rejected':rejected
    }
    return render(request, 'bank_officer/dashboard.html', data)

def review (request):
    loans = Loans.objects.filter(status='For Review')
    data = {
        'loans' : loans,
    }
    return render(request, 'bank_officer/review.html', data)

def approved (request):
    loans = Loans.objects.filter(status='Approved')
    data = {
        'loans' : loans,
    }
    return render(request, 'bank_officer/approved.html', data)

def rejected (request):
    loans = Loans.objects.filter(status='Rejected')
    data = {
        'loans' : loans,
    }
    return render(request, 'bank_officer/rejected.html', data)

def view_loan_app(request,pk):
    loan = Loans.objects.get(id=pk)
    data = {
        'loan' : loan,
    }
    return render(request, 'bank_officer/loan-app.html', data) 

def approve_loan_app(request,pk):
    loan = Loans.objects.get(id=pk)
    loan.status = "Approved"
    loan.save()
    data = {
        'loan' : loan,
    }
    return redirect ('review')

def reject_loan_app(request,pk):
    loan = Loans.objects.get(id=pk)
    loan.status = "Rejected"
    loan.save()
    data = {
        'loan' : loan,
    }
    return redirect ('review')

    

# Generate Loan App to PDF
def fetch_resources(uri, rel):
    path = os.path.join(uri.replace(settings.STATIC_URL, ""))
    return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GeneratePDF(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            loan = Loans.objects.get(id=pk)
        except:
            return HttpResponse("505 Not Found")
        data = {
            'loan' : loan,
        }
        pdf = render_to_pdf('bank_officer/loan-pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def logout_page(request):
    logout(request)
    print("it worked until here tho")
    return render(request, "main/home.html")