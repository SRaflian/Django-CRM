from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.Record_dashboard, name='record-dashboard'),
    path('record-view/', views.Record_view, name='record-view'),
    path('record/<int:id>/', views.customer_record_view, name='customer_record'),
    path('record/add/', views.add_record, name='add_record'),
    path('record/<int:id>/delete/', views.delete_record, name='delete_record'),
    path('record/edit/<int:id>/', views.edit_record, name='edit_record'),
]


