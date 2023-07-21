# import
from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, index, BookingView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("menu", MenuItemsView.as_view(), name="menu"),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name="single_menu_item"),
    path("booking", BookingView.as_view(), name="booking"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', index, name='index')
]
