from django.urls import path
from . import views



urlpatterns = [
    path('', views.artifact_list, name='artifact_list'),
    path('room/<int:i>',views.room, name = "lola"),
    path('custfeed',views.customer_feedback, name = 'customer_feedback')
    ]
