from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.my_custom_login_view, name='my_custom_login'),
    path('logout/', views.my_custom_logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('account/details/', views.account_details, name='account_details'),
    path('account/edit/', views.edit_account, name='edit_account'),
]