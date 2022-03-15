from rest_framework import serializers
from companies.models import Company

class CompanySerializerDisplay(serializers.ModelSerializer):

    employees = serializers.CharField(source='get_employee_сount_display')
    country = serializers.CharField(source='get_location_display')
    
    class Meta:
        model = Company
        fields = [
            'name','year_established','main_products', 
            'country', 'address', 'employees',
            'transaction_count', 'transaction_amount'
            ]
        # fields = "__all__"
        read_only_fields=('id','transaction_count','transaction_amount')


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = "__all__"

    read_only_fields=('id','transaction_count','transaction_amount')
    