from django.urls import path
from core import views

urlpatterns = [
    path('new/', views.new, name='new'),
]
