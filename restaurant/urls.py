from django.urls import path

from .views import say_welcome

urlpatterns = [path("", say_welcome, name="say_hello")]
