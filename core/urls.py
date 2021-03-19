from django.urls import path
from core import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
]
