from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
import datetime

class AccountReg(models.Model):
    SEX = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widow'),
    )

    PREFIX = (
        ('MR', 'Mr.'),
        ('MRS', 'Mrs.'),
        ('MS', 'Ms.'),
    )

    YEARS= [x for x in range(1940,2022)]

    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100, choices=SEX)
    marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS)
    birth_date= models.DateField(blank=True, null=True)
    email = models.EmailField()
    prefix = models.CharField(max_length=100, choices=PREFIX)
    phone = PhoneNumberField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return '{} - {}'.format(self.user,self.email)