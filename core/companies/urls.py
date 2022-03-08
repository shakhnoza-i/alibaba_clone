from django.urls import path, include
from companies.views import CompanyList, CompanyDetail


urlpatterns = [
    path('',  CompanyList.as_view(), name='companies-list'),
    path('<int:pk>/',  CompanyDetail.as_view(), name='company-details'),
]
