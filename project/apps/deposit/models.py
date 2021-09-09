from django.db import models
from django.core import validators
from django.utils.safestring import mark_safe
from random import randint, choice
import uuid
import string

"""
The models declared for this app are:
1. Company
2. Client
3. Storage or Warehouse

These models will set all the logic for the warehouses api. 

"""

#generate 
def generador(n):
    return ''.join([choice(string.ascii_letters + string.digits) for i in range(n)])

#This model declares the company model
class Company(models.Model):
    name = models.CharField(
        'Name',
        max_length=100,
        blank=False, 
        null=False
    )
    address = models.TextField(
        'Address',
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        
        
    def __str__(self):
        return self.name 
    

# In this model we declare the data for the customer.
class Client(models.Model):
    rut = models.CharField(
        'RUT',
        max_length=12, 
        blank=False, 
        null=False,
        unique=True
    )
    
    first_name = models.CharField(
        'First Name',
        max_length=50, 
        null=False,
        blank=False
    )
    
    last_name = models.CharField(
        'Last Name',
        max_length=50,
        null=False,
        blank=False 
    )
    company = models.ForeignKey(
        'Company', 
        related_name='bussiness', 
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return "%s - %s %s" % (self.rut, self.first_name, self.last_name)

class Product(models.Model):
    code_product = models.CharField(
        'Code',
        max_length=50,
        blank=True,
        null=True,
        editable=False,
        validators=[validators.MinLengthValidator(3)],
    )
    
    name = models.CharField(
        'Name', 
        max_length = 50,
        null=False,
        blank=False    
    )
    description = models.CharField(
        'Short Description',
        max_length = 300,
        null=True,
        blank=True
    )
    
    pic = models.ImageField(
        'Pic',
        upload_to='pic_product/',
        null=True,
        blank=True,
    )

    date_created = models.DateField(
        'Date created',
        auto_now_add=True
    )
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" height="100" />' % (
            self.pic.url))  # Get Image url

    image_tag.short_description = 'Image'
    
    def create_code_product(self):
        auto_id = generador(10)

        if not Product.objects.filter(code_product=auto_id).exists():
            self.code_product = auto_id

        
    def save(self, *args, **kwargs):
        if not self.code_product:
            self.create_code_product()

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name 
    
 
class Storage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.IntegerField(
        'Amount',
    )
    pricing = models.CharField(
        'Pricing',
        max_length=10,
        null=False,
        blank=False
    )
    update_date = models.DateField(
        'Update date',
        auto_now=False,
        auto_now_add=False
    )
    date_created = models.DateField(
        'Date created',
        auto_now_add=True
    )

    class Meta: 
        verbose_name = 'Storage'
        verbose_name_plural = 'Storages'
        
    def __str__(self):
        return '%s %s' % (self.product, self.amount)
    
    
class Request(models.Model):
    client = models.ForeignKey(
        'Client', 
        on_delete=models.CASCADE
    )
    address_delivery = models.TextField(
        'Address',
        max_length=300, 
        blank=True, 
        null=True
    )
    product = models.ForeignKey(
        'Product', 
        on_delete=models.CASCADE
    )
    
    amount_request = models.IntegerField(
        'Amount',
    )
    
    
    is_approved = models.BooleanField("is it approved?", default=False)
    
    created_request = models.DateTimeField(
        'Datetime from created request', 
        auto_now_add=True
    )
    
    
    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
        
        
    def __str__(self):
        return '%s %s' %s(self.client, self.product)
    