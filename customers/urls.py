from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.Record_dashboard, name='record-dashboard'),
    path('record/<int:id>/', views.customer_record_view, name='customer_record'),
    path('record/add/', views.add_record, name='add_record'),
]


