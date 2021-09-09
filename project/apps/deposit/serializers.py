from django.contrib.auth import authenticate
from rest_framework import serializers 
from apps.deposit.models import (
    Company,
    Client,
    Product,
    Storage,
    Request
)

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)
    class Meta:
        model = Client
        fields = (
            'id',
            'rut',
            'first_name',
            'last_name',
            'company'
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'code_product',
            'name',
            'description',
            'pic'
        ]

class StorageSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False,)
    class Meta:
        model = Storage
        fields = (
            'id',
            'product',
            'amount',
            'update_date',
            'date_created'
        )
        
class RequestSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Request
        fields = (
            'id',
            'client',
            'address_delivery',
            'product',
            'amount_request',
        )