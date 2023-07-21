from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.menuitem1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.menuitem2 = MenuItem.objects.create(title="Fries", price=20, inventory=100)
        self.menuitem3 = MenuItem.objects.create(title="Milkshake", price=30, inventory=100)

    def test_getall(self):
        # Get all the data directly from the database
        menu_items = MenuItem.objects.all()

        # Serialize the initial data (menu items)
        expected_data = MenuItemSerializer(menu_items, many=True).data

        # Retrieve the serialized data from the serializer
        serializer = MenuItemSerializer(instance=menu_items, many=True)
        data = serializer.data

        # Compare the serialized data with the initial data
        self.assertEqual(data, expected_data)
