from django.urls import path
from .views import search_invoices

urlpatterns = [
    path('search/', search_invoices, name='search_invoices'),
]
