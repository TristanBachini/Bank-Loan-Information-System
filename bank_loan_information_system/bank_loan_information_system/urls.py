"""bank_loan_information_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),
    path('auth/', include("login_app.urls")),
    path('navbar/', include("navbar.urls")),
    path('loan-calculator/', include("bank_calculator.urls")),
    path('view-loan-applications/', include("loans_borrower.urls")),
    path('bank-officer/', include("bank_officer.urls")),
]
