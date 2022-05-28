from django.db import models
from django.contrib.auth.models import User

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
        ('Owned', 'Owned'),
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

    status = models.CharField(max_length=100, choices=STATUS, null=True)

    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    sell_price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    dp_percent = models.IntegerField(null=True, blank=True)
    dp_amt = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    loan_amt = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    no_of_payments = models.IntegerField(null=True, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    civ_status = models.CharField(max_length=100, choices=CIV_STATUS, null=True, blank=True)

    unit_no = models.CharField(max_length=100, null=True, blank=True)
    condo_name = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    subdiv_brgy = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    municip_prov = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    len_stay = models.CharField(max_length=100, choices=LEN_STAY, null=True, blank=True)
    len_stay_num = models.IntegerField(null=True, blank=True)
    home_own = models.CharField(max_length=100, choices=HOME_OWN, null=True, blank=True)

    phone_type = models.CharField(max_length=100, choices=PHONE_TYPE, null=True, blank=True)
    home_num = models.CharField(max_length=100, null=True, blank=True)
    mobile_num = models.CharField(max_length=100, null=True, blank=True)
    email_add = models.CharField(max_length=100, null=True, blank=True)

    prime_income = models.CharField(max_length=100, choices=PRIME_INCOME, null=True, blank=True)

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
    
    # int_rate = models.CharField(max_length=50, null=True)
    # principal = models.IntegerField(null=True, blank=True)
    # rem_bal = models.IntegerField(null=True, blank=True)
    # next_due = models.DateField(null=True)

    def __str__(self):
        return "{}, {} - {}".format(self.last_name, self.first_name, self.id)



 
