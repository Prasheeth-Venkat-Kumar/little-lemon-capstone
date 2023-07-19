from django.shortcuts import render
from rest_framework import generics
# import serializers
from .serializers import BookingSerializer, MenuItemSerializer
# import models
from .models import Booking, MenuItem
# import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, "index.html", {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer