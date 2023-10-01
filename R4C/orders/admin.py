from django.contrib import admin

from .models import Order


# Регистрируем модель Заказа в админ-панели
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'robot_serial', 'robot_model', 'robot_version', 'robot_created', 'robot_quantity')
