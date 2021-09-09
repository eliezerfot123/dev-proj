from django.urls import path, include
from apps.landing.views import (
    LandingView, 
)

urlpatterns = [
    path('', LandingView.as_view(), name="index"),
] 