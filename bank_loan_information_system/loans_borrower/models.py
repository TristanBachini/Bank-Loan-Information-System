from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Loans(models.Model):
    STATUS = (
        ('For Review', 'For Review'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    CIV_STATUS = (
        ('Married', 'Married'),
        ('Separated', 'Separated'),
        ('Single', 'Single'),
        ('Widower', 'Widower'),
    )

    LEN_STAY = (
        ('Months', 'Months'),
        ('Years', 'Years'),
    )

    HOME_OWN = (
        ('Mortgage', 'Mortgage'),
        ('Rented', 'Rented'),
        ('Owned', 'Owned'),
        ('Used Free/Living with Parents/Relatives', 'Used Free/Living with Parents/Relatives'),
    )

    PHONE_TYPE = (
        ('Home', 'Home'),
        ('Mobile', 'Mobile'),
    )

    PRIME_INCOME = (
        ('Employment', 'Employment'),
        ('Business', 'Business'),
    )

    EMP_TYPE = (
        ('Local(Government)', 'Local(Government)'),
        ('Local(Private)', 'Local(Private)'),
        ('OFW Non-Immigrant(Government)', 'OFW Non-Immigrant(Government)'),
        ('OFW Non-Immigrant(Private)', 'OFW Non-Immigrant(Private)'),
    )

    LOAN_TAG = (
        ('For Review', 'For Review'),
        ('Delinquent', 'Delinquent'),
        ('In-Loan Default', 'In-Loan Default'),
        ('Completed', 'Completed'),
    )

    app_date = models.DateTimeField(null=True, blank=True)

    status = models.CharField(default='For Review',max_length=100, choices=STATUS, null=True)

    make = models.CharField(max_length=100, null=True, blank=False)
    model = models.CharField(max_length=100, null=True, blank=False)
    sell_price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=False)
    dp_percent = models.PositiveIntegerField(null=True, blank=False)
    dp_amt = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=False)
    loan_amt = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=False)
    no_of_payments = models.IntegerField(null=True, blank=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=False)
    birthdate = models.DateField(null=True, blank=False)
    civ_status = models.CharField(max_length=100, choices=CIV_STATUS, null=True, blank=False)

    unit_no = models.CharField(max_length=100, null=True, blank=False)
    condo_name = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=False)
    subdiv_brgy = models.CharField(max_length=100, null=True, blank=False)
    city = models.CharField(max_length=100, null=True, blank=False)
    municip_prov = models.CharField(max_length=100, null=True, blank=False)
    country = models.CharField(max_length=100, null=True, blank=False)
    len_stay = models.CharField(max_length=100, choices=LEN_STAY, null=True, blank=False)
    len_stay_num = models.IntegerField(null=True, blank=False)
    home_own = models.CharField(max_length=100, choices=HOME_OWN, null=True, blank=False)

    phone_type = models.CharField(max_length=100, choices=PHONE_TYPE, null=True, blank=False)
    home_num = models.CharField(max_length=100, null=True, blank=True)
    mobile_num = PhoneNumberField(max_length=100, null=True, blank=True)
    email_add = models.CharField(max_length=100, null=True, blank=False)

    prime_income = models.CharField(max_length=100, choices=PRIME_INCOME, null=True, blank=False)

    emp_type = models.CharField(max_length=100, choices=EMP_TYPE, null=True, blank=True)
    emp_name = models.CharField(max_length=100, null=True, blank=True)
    job_pos = models.CharField(max_length=100, null=True, blank=True)
    emp_tenure = models.CharField(max_length=100, choices=LEN_STAY, null=True, blank=True)
    emp_tenure_num = models.IntegerField(null=True, blank=True)
    emp_monthly_income = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    emp_work_no = models.CharField(max_length=100, null=True, blank=True)

    bsns_type = models.CharField(default="Self-Employed", max_length=100, null=True, blank=True)
    bsns_name = models.CharField(max_length=100, null=True, blank=True)
    bsns_tenure = models.CharField(max_length=100, choices=LEN_STAY, null=True, blank=True)
    bsns_tenure_num = models.IntegerField(null=True, blank=True)
    bsns_monthly_income = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    bsns_work_no = models.CharField(max_length=100, null=True, blank=True)

    bsns_unit_no = models.CharField(max_length=100, null=True, blank=True)
    bsns_condo_name = models.CharField(max_length=100, null=True, blank=True)
    bsns_street = models.CharField(max_length=100, null=True, blank=True)
    bsns_subdiv_brgy = models.CharField(max_length=100, null=True, blank=True)
    bsns_city = models.CharField(max_length=100, null=True, blank=True)
    bsns_municip_prov = models.CharField(max_length=100, null=True, blank=True)
    bsns_country = models.CharField(max_length=100, null=True, blank=True)

    loan_docs = models.FileField(upload_to='loan_docs/', null=True, blank=True)
    
    loan_tag = models.CharField(max_length=100, choices=LOAN_TAG, null=True, blank=True)

    def __str__(self):
        return "{}, {} - {}".format(self.last_name, self.first_name, self.id)



 
