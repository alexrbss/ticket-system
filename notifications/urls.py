from django.urls import path
from .views import NotificationListCreateAPIView, NotificationDetailAPIView

app_name = 'notifications'

urlpatterns = [
    path('', NotificationListCreateAPIView.as_view(), name='notification-list-create'),
    path('<int:pk>/', NotificationDetailAPIView.as_view(), name='notification-detail'),
]