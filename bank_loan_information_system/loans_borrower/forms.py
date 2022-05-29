from django import forms
from .models import *

class LoanApplyForm(forms.ModelForm):
    class Meta:
        model = Loans
        fields = '__all__'
        # widgets = {
        #     'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        # }