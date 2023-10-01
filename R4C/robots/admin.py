from django.contrib import admin

from .models import Robot


# Регистрируем модель Робота в админ-панели
@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ('serial', 'model', 'version', 'created', 'quantity')
