from django.contrib import admin
from apps.deposit.models import (
    Company,
    Client,
    Product,
    Storage,
    Request
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'rut',
        'first_name',
        'last_name',
        'company'
    ]
    search_fields = (
        'rut',
        'first_name',
        'last_name',
        'company',
    )
    list_filter = (
        'rut',
        'company',
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'code_product',
        'name',
        'image_tag',
        'date_created'
    ]
    search_fields = (
        'code_product',
        'name',
    )


    

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'amount',
    ]
        
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'product',
        'amount_request',
        'is_approved'
    ]