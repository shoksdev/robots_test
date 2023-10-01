from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('orders/', include('orders.urls')),
    path('robots/', include('robots.urls')),
    path('admin/', admin.site.urls),
]
