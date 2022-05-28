from django import forms

TYPE_SELECT = (
    ('0', 'Female'),
    ('1', 'Male'),
)

MARITAL_STATUS = (
    ('0', 'Single'),
    ('1', 'Married'),
    ('2', 'Divorced'),
    ('3', 'Widow'),
)

PREFIX = (
    ('0', 'Mr.'),
    ('1', 'Mrs.'),
    ('2', 'Ms.'),
)

YEARS= [x for x in range(1940,2022)]


class AccountRegForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    sex = forms.CharField(label='Sex', widget=forms.RadioSelect(choices=TYPE_SELECT))
    marital_status = forms.CharField(label='Marital Status', widget=forms.RadioSelect(choices=MARITAL_STATUS))
    birth_date= forms.DateField(label='What is your birth date?', initial="1990-06-21", widget=forms.SelectDateWidget(years=YEARS))
    email = forms.EmailField(
        label=("E-mail"),
        required=True,
        widget=forms.TextInput(
            attrs={"type": "email",
                   "size": "30",
                   "placeholder":('E-mail address')})
    )
    prefix = forms.CharField(label='Prefix', widget=forms.Select(choices=PREFIX))