from django.urls import path 
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('review', views.review, name="review"),
    path('approved', views.approved, name="approved"),
    path('rejected', views.rejected, name="rejected"),
    path('logout/',views.logout_page, name="logout"),
    path('view-loan-app/<str:pk>', views.view_loan_app, name="loan-app"),
    path('download-loan-app/<int:pk>', views.GeneratePDF.as_view(), name="generate-pdf"),
]