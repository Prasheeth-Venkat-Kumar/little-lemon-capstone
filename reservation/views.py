from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemSerializer
# Create your views here.
from rest_framework import generics

# Create your views here.
class MenuItemViewSet(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer



