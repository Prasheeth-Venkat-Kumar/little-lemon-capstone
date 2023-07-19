from django.shortcuts import render
from rest_framework import generics
# import serializers
from .serializers import BookingSerializer, MenuItemSerializer
# import models
from .models import Booking, MenuItem

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer