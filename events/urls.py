from django.urls import path
from .views import EventListCreateAPIView, EventDetailAPIView

app_name = 'events'

urlpatterns = [
    path('', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
]
