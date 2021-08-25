from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/<show_id>/edit', views.edit),
    path('shows/<show_id>/delete', views.delete),
    path('shows/<show_id>', views.detalle),
]
