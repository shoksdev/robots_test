from django.contrib import admin

from .models import Customer


# Регистрируем модель Покупателя в админ-панели
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', )
