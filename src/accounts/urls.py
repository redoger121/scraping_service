from django.contrib import admin
from django.urls import path
from .views import *
from accounts.views import login_view, logout_view
urlpatterns = [

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('update/', update_view, name='update'),
    path('delete/', delete_view, name='delete'),

]
