from django.db import models
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, default="")
    no_of_guests = models.SmallIntegerField(default=1)
    booking_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.name} for {self.no_of_guests} guests on {self.booking_date}"
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255, default="")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f"{self.title} : {self.price}"
