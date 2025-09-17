from django.urls import path
from .views import CustomerListCreateAPIView, CustomerDetailAPIView

app_name = 'customers'

urlpatterns = [
    path('', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
]