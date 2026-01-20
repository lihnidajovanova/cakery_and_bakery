from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_cake_page, name='add_cake_page'),
]