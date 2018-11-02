from django.shortcuts import render
from .models import ArtifactDetail


def artifact_list(request):
    artifacts = ArtifactDetail.objects.order_by('room_no')
    return render(request, 'details/artifact_list.html', {'artifacts':artifacts})
    
