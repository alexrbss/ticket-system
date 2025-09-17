from django.urls import path
from .views import TicketListCreateAPIView, TicketDetailAPIView

app_name = 'tickets'

urlpatterns = [
    path('', TicketListCreateAPIView.as_view(), name='ticket-list-create'),
    path('<int:pk>/', TicketDetailAPIView.as_view(), name='ticket-detail'),
]