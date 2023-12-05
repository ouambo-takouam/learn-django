from django.urls import path

from . import views
from .views import (
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView
)

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name='lead_delete'),
]
