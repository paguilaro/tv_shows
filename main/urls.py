from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.index),
    path('register', views.register),
    path('login', views.login), 
    path('logout', views.logout), 
    path('shows/new', views.new),
    path('shows/<show_id>/edit', views.edit),
    path('shows/<show_id>/delete', views.delete),
    path('shows/<show_id>', views.detalle),
]
