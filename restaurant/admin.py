from django.contrib import admin

from .models import Booking, Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "inventory")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "guest_id", "booking_date")
