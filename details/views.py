from django.shortcuts import render
from .models import ArtifactDetail
import os
from django.conf import settings

#if a new artifact is added to an already present room... we haven't considered that.....yet

file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'numbers.txt')
f = open(file_path,'r')
no_of_rooms = f.read()
f.close()

'''
room_template = """
{% load static %}
<html>
    <head>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
      <link rel="stylesheet" href="{% static 'css/details.css' %}">
      <link href="https://fonts.googleapis.com/css?family=Patrick+Hand" rel="stylesheet">
        <title>Artifact List {{artif}}</title>
    </head>
    <body>

        <div class="page-header">
            <h1><a href="/">Artifact List</a></h1>
        </div>



{% for artifact in artifacts %}
    <div class = "artifact">
      <br>
      <br>
      <br>
        <h1><a href="">{{ artifact.artifact_name }}</a></h1>
        <p>Room number : {{ artifact.room_no }} , Artifact number: {{ artifact.artifact_no}} </p>
        <p>{{ artifact.artifact_description|linebreaksbr }}</p>
      <br>
      <br>
    </div>
{% endfor %}

</body>
</html>
"""
'''


def artifact_list(request):
    artifacts = ArtifactDetail.objects.filter(room_no__contains="").order_by('room_no')
    return render(request, 'details/artifact_list.html', {'artifacts':artifacts})


def artifacts_in_room(room_no):
    artifacts = ArtifactDetail.objects.filter(room_no__contains=room_no)
    return artifacts

artifacts_in_room(1)

def room_no(i,request):
    artifacts = artifacts_in_room()
    return render(request, 'details/room_number1.html', {'artifacts' : artifacts})

def make_html():
    for i in range(int(no_of_rooms)+1):
        fila=open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates/details/'+"room_number"+str(i+1)+".html"),'w+')
        artifacts_in_room = ArtifactDetail.objects.filter(room_no__contains = str(i))

        #fila.write(room_template)
        fila.close()



make_html()
