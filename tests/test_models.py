from django.test import TestCase
from restaurant.models import MenuItem
from decimal import Decimal

class TestMenuItem(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        expected_string = "IceCream : 80"  # The expected string representation
        self.assertEqual(str(item), expected_string)  
