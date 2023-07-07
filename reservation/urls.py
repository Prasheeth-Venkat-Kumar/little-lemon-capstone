from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path("menuitems/", views.MenuItemViewSet.as_view()),
    path("menuitems/<int:pk>/", views.SingleMenuItemViewSet.as_view()),
]