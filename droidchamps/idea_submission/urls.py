from django.urls import path
from . import views

urlpatterns = [
    path('', views.ideaform, name='ideaform'),
    # Add more paths here as needed
]