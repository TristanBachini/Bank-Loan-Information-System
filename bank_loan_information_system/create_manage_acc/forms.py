from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, CharField, HiddenInput, NumberInput,CheckboxInput
from .models import AccountReg, BankAccount
from django.forms.widgets import DateInput, Select, RadioSelect
import datetime
from phonenumber_field.formfields import PhoneNumberField

# TYPE_SELECT = (
#     ('0', 'Female'),
#     ('1', 'Male'),
# )

# MARITAL_STATUS = (
#     ('0', 'Single'),
#     ('1', 'Married'),
#     ('2', 'Divorced'),
#     ('3', 'Widow'),
# )

# PREFIX = (
#     ('0', 'Mr.'),
#     ('1', 'Mrs.'),
#     ('2', 'Ms.'),
# )

# YEARS= [x for x in range(1940,2022)]


class AccountRegForm(ModelForm):
    # first_name = forms.CharField(label='First name', max_length=100)
    # last_name = forms.CharField(label='Last name', max_length=100)
    # sex = forms.CharField(label='Sex', widget=forms.RadioSelect(choices=TYPE_SELECT))
    # marital_status = forms.CharField(label='Marital Status', widget=forms.RadioSelect(choices=MARITAL_STATUS))
    # birth_date= forms.DateField(label='What is your birth date?', initial="1990-06-21", widget=forms.SelectDateWidget(years=YEARS))
    # email = forms.EmailField(
    #     label=("E-mail"),
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={"type": "email",
    #                "size": "30",
    #                "placeholder":('E-mail address')})
    # )
    # prefix = forms.CharField(label='Prefix', widget=forms.Select(choices=PREFIX))
    # phone = PhoneNumberField()
    # address = forms.CharField(label='Last name', max_length=300)
    class Meta:
        model = AccountReg
        fields = "__all__"
        widgets = {
            'user':  HiddenInput(attrs={'type': 'hidden'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control input-area', 'placeholder': 'First name', 'required' : True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'aria-label': 'Last name', 'required': True}),
            'prefix':  Select(attrs={'class': 'form-control'}),
            'sex':  Select(attrs={'class': 'form-control'}),
            'marital_status':  Select(attrs={'class': 'form-control'}),
            'phone' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile', 'aria-label': 'Mobile', 'required': False}),
            'birth_date': DateInput({'class': 'form-control', 'type': 'date'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'aria-label': 'Email', 'required': True}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address', 'aria-label': 'Address', 'required': True}),
        }

class BankAccountForm(ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'
        widgets = {
            'user':  HiddenInput(attrs={'type': 'hidden'}),
            'balance' : forms.NumberInput(attrs={'required': False, 'disabled': True}),
            'deposit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }