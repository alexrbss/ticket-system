from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.
class NotificationListCreateAPIView(APIView):
    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotificationDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Notification, pk=pk)

    def get(self, request, pk):
        notification = self.get_object(pk)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

    def put(self, request, pk):
        notification = self.get_object(pk)
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notification = self.get_object(pk)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
