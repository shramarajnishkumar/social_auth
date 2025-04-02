from django.urls import path
from .views import FacebookCallback

urlpatterns = [
    path("callback/", FacebookCallback.as_view(), name="facebook_callback"),

]