from django.urls import path
from . import views

urlpatterns = [
    path('', views.artifact_list, name='artifact_list'),
]
