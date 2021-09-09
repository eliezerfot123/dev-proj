from django.contrib.auth.models import User
# third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from apps.deposit.serializers import StorageSerializer, RequestSerializer
from apps.deposit.models import (
    Company,
    Client,
    Product,
    Storage,
    Request
)

#create new storage 
class StorageCreateApi(generics.CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    

#list storage with product
class StorageApi(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    
    
#list request with product
class RequestApi(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
    
#create new request 
class RequestCreateApi(mixins.ListModelMixin, generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        serializer = RequestSerializer(data=request.data)
        client_selected = Client.objects.get(id=request.POST.get('client'))
        product_select = Product.objects.get(id=request.POST.get('product'))
        #make the comprabations 
        storage = Storage.objects.get(product__id=request.POST.get('product'))
        if storage: 
            #validate availability
            amount = storage.amount
            amount_request = request.POST.get('amount_request')
            amount_request = int(amount_request)
            subtract = amount - amount_request
            if amount != 0 and amount >= amount_request:
                
                #save data on request 
                Request.objects.create(
                    client=client_selected,
                    address_delivery = request.POST.get('address_delivery'),
                    product=product_select,
                    amount_request=amount_request,
                    is_approved = True
                )
                #update amount on the storage
                storage.amount = subtract
                storage.save()
                
                if serializer.is_valid():
                    return Response(
                        serializer.data,
                        {"detail": "Registration was successful"}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                if serializer.is_valid():
                    Request.objects.create(
                        client=client_selected,
                        address_delivery = request.POST.get('address_delivery'),
                        product=product_select,
                        amount_request=amount_request,
                        is_approved = False
                    )
                    return Response(
                        {"detail": "Sorry, Product quantity not found"}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
        return self.create(request, *args, **kwargs)

    
