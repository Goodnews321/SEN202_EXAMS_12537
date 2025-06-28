from rest_framework import serializers
from .models import Manager, Address


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = 'has_company_card'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

