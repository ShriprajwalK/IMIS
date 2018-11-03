from django.urls import path
from django.conf import settings
#from django.conf.urls.static
from . import views



urlpatterns = [
    path('', views.artifact_list, name='artifact_list'),
    path('room/<int:i>',views.room, name = "lola"),
    path('search',views.search,name = 'search'),
    path('feedback', views.feedback, name = "feedback"),
    path('success.html',views.success, name = 'success'),
    path('aravind',views.aravind,name = 'aravind')
    ] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
