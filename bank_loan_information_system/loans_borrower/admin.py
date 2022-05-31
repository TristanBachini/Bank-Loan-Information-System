from django.contrib import admin
from create_manage_acc.models import BankAccount

from loans_borrower.models import Loans

from create_manage_acc.models import AccountReg

# Register your models here.

admin.site.register(Loans)
admin.site.register(AccountReg)
admin.site.register(BankAccount)
