from django.db import models
from customers.models import Customer

# Create your models here.
class Notification(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.id} for {self.customer.name}"
