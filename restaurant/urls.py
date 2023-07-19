# import
from django.urls import path
from .views import MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("menu", MenuItemsView.as_view(), name="menu"),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name="single_menu_item"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
