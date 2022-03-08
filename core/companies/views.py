from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer   
    filter_backends = (filters.DjangoFilterBackend, SearchFilter ,OrderingFilter)
    filter_fields = ('employee_сount', 'location',)
    ordering =('name',)
    search_fields =('name', 'main_products',)


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
