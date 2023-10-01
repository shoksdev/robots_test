from django.urls import path

from .views import download_excel_report, create_robot

urlpatterns = [
    path('download-excel/', download_excel_report, name='download_excel'),  # отрабатывает функция, отвечающая за
    # скачку excel-файла с детализацией по всем роботам
    path('create/', create_robot, name='create_robot'),  # отрабатывает функция, отвечающая за создание нового робота
]
