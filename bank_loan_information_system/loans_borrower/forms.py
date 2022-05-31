from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

class LoanApplyForm(forms.ModelForm):
    mobile_num = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget, required=False,
    )
    mobile_num.widget.attrs = {'class': 'form-control', 'placeholder': '+63'}
    birthdate = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'mm/dd/yyyy',
                     'data-target': '#datetimepicker1'},
                     format='%m/%d/%y'
        ),
        required=False
    )
    class Meta:
        model = Loans
        fields = '__all__'
        widgets = {
            'app_date': forms.HiddenInput(attrs={'type': 'hidden'}),

            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}),

            # Loan Deets
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Make'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model'}),
            'sell_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Sell Price'}),
            'dp_percent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Down-payment %'}),
            'dp_amt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Down-payment'}),
            'loan_amt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Loan'}),
            'no_of_payments': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'No. of Payments'}),

            # User Deets
            'user': forms.HiddenInput(attrs={'type': 'hidden'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'civ_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Civil Status'}),

            # User address
            'unit_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit no.'}),
            'condo_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Condominium'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street'}),
            'subdiv_brgy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subdivision/Barangay'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'municip_prov': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Municipality/Province'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'len_stay': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Length of Stay'}),
            'len_stay_num': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Length of Stay no.'}),
            'home_own': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ownership'}),

            # User contact
            'phone_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Type of Phone'}),
            'home_num': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Home no.'}),
            'email_add': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),

            'prime_income': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Primary Income'}),

            # If employment
            'emp_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Employment Type'}),
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Employer's Name"}),
            'job_pos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Position'}),
            'emp_tenure': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tenure'}),
            'emp_tenure_num': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tenure no.'}),
            'emp_monthly_income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monthly Income'}),
            'emp_work_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Work no.'}),

            # If business
            'bsns_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Type'}),
            'bsns_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Business Name"}),
            'bsns_tenure': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tenure'}),
            'bsns_tenure_num': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tenure no.'}),
            'bsns_monthly_income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monthly Income'}),
            'bsns_work_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Work no.'}),
            
            # Business Deets
            'bsns_unit_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Unit no."}),
            'bsns_condo_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Condominium"}),
            'bsns_street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Street"}),
            'bsns_subdiv_brgy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Subdivision/Barangay"}),
            'bsns_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "City"}),
            'bsns_municip_prov': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Municipality/Province"}),
            'bsns_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Country"}),
        }