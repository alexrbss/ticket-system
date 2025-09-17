from django.db import models
from events.models import Event
from customers.models import Customer

# Create your models here.
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.event.name} - {self.customer.name}"
