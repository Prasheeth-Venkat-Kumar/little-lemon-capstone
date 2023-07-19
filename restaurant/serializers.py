from rest_framework import serializers
from .models import MenuItem, Booking

class MenuItemSerializer(serializers.ModelSerializer):
    # set id to read only
    id = serializers.ReadOnlyField()
    class Meta:
        model = MenuItem
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Booking
        fields = "__all__"