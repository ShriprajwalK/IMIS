from django.shortcuts import render
from .models import ArtifactDetail
import os
from django.conf import settings

file_path = os.path.join(settings.STATIC_ROOT, 'numbers.txt')


t1 = ArtifactDetail.objects.filter(room_no__contains="")

def get_query1():
    k = {i.room_no for i in t1}
    return k
count1 = len(get_query1())

room_template = """
{% load static %}
<html>
    <head>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
      <link rel="stylesheet" href="{% static 'css/details.css' %}">
      <link href="https://fonts.googleapis.com/css?family=Patrick+Hand" rel="stylesheet">
        <title>Artifact List</title>
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



def artifact_list(request):
    artifacts = ArtifactDetail.objects.order_by('room_no')
    return render(request, 'details/artifact_list.html', {'artifacts':artifacts})

t2 = ArtifactDetail.objects.filter(room_no__contains="")

def get_query2():
    k = {i.room_no for i in t2}
    return k

count2 = len(get_query2())

def make_html():
    if count2 - count1 !=0:
        for i in range(count2-count1):
            with open('templates/details/'+"room_number"+str(count1+i+1)+".html",'w+') as f:
                f.write(room_template)

make_html()
