from django.urls import path
from . import views

urlpatterns = [
    path('sample', views.dashboard, name='dashboard'),
    path('add_invoice', views.AddInvoice.as_view(), name='add_invoice'),
    path('list_invoice', views.InvoiceList.as_view(), name='list_invoice'),
    path('<int:pk>', views.InvoiceDetail.as_view(), name='invoice_detail'),
    path('pdf/<int:pk>', views.InvoicePdf, name='invoice_view'),


    ]
