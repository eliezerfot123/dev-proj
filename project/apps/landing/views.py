from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from apps.deposit.models import Storage


# Create your views here.
class LandingView(View):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        
        search = Storage.objects.all()
        
        return render(request, 'index.html', {'search':search})