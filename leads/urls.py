from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('<int:lead_id>/', views.lead_detail, name='lead_detail'),
    path('create/', views.lead_create, name='lead_create'),
]
