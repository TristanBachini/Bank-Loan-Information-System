from django import forms

TYPE_SELECT = (
    ('0', 'Female'),
    ('1', 'Male'),
)

class AccountRegForm(forms.Form):

    sex = forms.CharField(label='Sex', widget=forms.RadioSelect(choices=TYPE_SELECT))