from django.urls import path
from . import views
from .models import ArtifactDetail

a = ArtifactDetail.objects.filter(room_no__contains="")
k = a[len(a)-1].room_no

urlpatterns = [
    path('', views.artifact_list, name='artifact_list'),
    path('room1',views.temp[0], name = 'room number 1'),

    ]
