from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('view-loan-apps', views.viewLoanApps, name="view-loan-apps"),
    path('view-loan-apps-info/<str:pk>', views.viewLoanAppsInfo, name="view-loan-apps-info"),
    path('loan-apply', views.loanApply, name="loan-apply"),
    path('loan-docs-upload/<str:pk>', views.loanDocsUpload, name="loan-docs-upload"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)