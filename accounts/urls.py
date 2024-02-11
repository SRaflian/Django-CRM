from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.my_custom_login_view, name='my_custom_login'),
    path('success/', views.success_view, name='some_success_url'),
    path('logout/', views.my_custom_logout_view, name='logout'),
]