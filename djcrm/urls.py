from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('leads.urls')),
    path('admin/', admin.site.urls),
]
