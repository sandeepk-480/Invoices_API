from django.urls import path
from app import views
urlpatterns = [
    path('', views.InvoiceApiList.as_view(), name='invoice'),
    path('<int:pk>/', views.InvoiceApiRUD.as_view(), name='invoice_rod'),

    path('detail/', views.InvoiceDetailList.as_view(), name='invoice_detail'),
    path('detail/<int:pk>/', views.InvoiceDetailRUD.as_view(), name='invoice_detail_rod'),
]
