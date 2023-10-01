from django.urls import path

# Импортируем функции из views.py
from .views import create_order

urlpatterns = [
    path('create/', create_order, name='create_order'),  # Создание заказа
]
