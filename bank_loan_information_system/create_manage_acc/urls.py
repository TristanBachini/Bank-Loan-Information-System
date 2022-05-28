from django.urls import path 
from . import views

urlpatterns = [
    path('create-account',views.account_registration,name="create-account"),
]