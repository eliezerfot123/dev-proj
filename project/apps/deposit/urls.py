from django.urls import path
from apps.deposit.api import (
    StorageCreateApi,
    StorageApi,
    RequestApi,
    RequestCreateApi
)

urlpatterns = [
    path('deposit/store/create',StorageCreateApi.as_view()),
    path('deposit/store/list',StorageApi.as_view()),
    path('deposit/request/list',RequestApi.as_view()),
    path('deposit/request/create',RequestCreateApi.as_view()),
]