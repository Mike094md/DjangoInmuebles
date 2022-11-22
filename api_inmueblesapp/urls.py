from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list,  name='user_list'),
    path('users/<int:pk>', views.user_detail,  name='user_detail'),
    path('properties/', views.property_list,  name='property_list'),
    path('properties/<int:pk>', views.property_detail,  name='property_detail'),
]