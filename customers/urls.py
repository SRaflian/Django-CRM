from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.Record_dashboard, name='record-dashboard'),
]


