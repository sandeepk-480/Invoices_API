from django.shortcuts import render
from app.models import InvoiceDetail, Invoice
from app.serializers import InvoiceDetailSerializer, InvoiceSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# CRUD For Invoice Model
class InvoiceApiList(ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceApiRUD(RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer



# CRUD For Invoice Detail Model
class InvoiceDetailList(ListCreateAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer

class InvoiceDetailRUD(RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer