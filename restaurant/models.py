from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()


class Booking(models.Model):
    name = models.CharField(max_length=255)
    guest_id = models.IntegerField()
    booking_date = models.DateTimeField()
