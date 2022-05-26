from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Loans(models.Model):
    STATUS = (
        ('For Review', 'For Review'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    app_no = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=100, null=True)
    loan_amt = models.IntegerField(null=True, blank=True)
    int_rate = models.CharField(max_length=50, null=True)
    no_of_payments = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, null=True)
    principal = models.IntegerField(null=True, blank=True)
    rem_bal = models.IntegerField(null=True, blank=True)
    next_due = models.DateField(null=True)

    def __str__(self):
        return "{}, {} - {}".format(self.last_name, self.first_name, self.app_no,)



 
