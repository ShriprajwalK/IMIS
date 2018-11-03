from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import ArtifactDetail
import os
from django.conf import settings
from django.http import HttpResponse
from details.forms import FeedbackForm

#if a new artifact is added to an already present room... we haven't considered that.....yet

file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'numbers.txt')
f = open(file_path,'r')
no_of_rooms = f.read()
f.close()

room_template = """
{% load static %}
<html>
    <head>
    <title>Artifact List {{artif}}</title>

      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
      <link rel="stylesheet" href="{% static 'css/details.css' %}">
      <link href="https://fonts.googleapis.com/css?family=Patrick+Hand" rel="stylesheet">
<style>
.collapsible {
    background-color: #777;
    color: white;
    cursor: pointer;
    padding: 18px;
    width: 100%;
    border: none;
    text-align: left;
    outline: none;
    font-size: 15px;
}

.active, .collapsible:hover {
    background-color: #555;
}

.collapse,#id {
    padding: 0 18px;
    display: none;
    overflow: hidden;
    background-color: #f1f1f1;
}
</style>
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
        <div class="container">
        <h1><p>{{ artifact.artifact_name }}</p></h1>
        <button class="collapsible">Artifact Information</button>
        <div id="demo" class="collapse">
        <p>Room number : {{ artifact.room_no }} , Artifact number: {{ artifact.artifact_no}} </p>
        {{ artifact.artifact_description|linebreaksbr }}
        </div></div>
    <br>
  <br>
{% endfor %}
<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>
 <input type='text' value='' placeholder='Search for...'>

<script>
$(document).ready(function() {
  var input = $('input');
  var button = $('button');

  //Create varialbe to store search field
  var toSearch = '';

  //Api data:
  var searchUrl = 'https://en.wikipedia.org/w/api.php';

  //.ajax() to get articles
   var ajaxArticl = function() {
  $.ajax({
        type: "GET",
        url: "http://en.wikipedia.org/w/api.php?action=parse&format=json&prop=text&section=0&page=Jimi_Hendrix&callback=?",
        contentType: "application/json; charset=utf-8",
        async: false,
        dataType: "json",
        success: function (data, textStatus, jqXHR) {

            var markup = data.parse.text["*"];
            var blurb = $('<div></div>').html(markup);

            // remove links as they will not work
            blurb.find('a').each(function() { $(this).replaceWith($(this).html()); });

            // remove any references
            blurb.find('sup').remove();

            // remove cite error
            blurb.find('.mw-ext-cite-error').remove();
            $('#article').html($(blurb).find('p'));

        },
        error: function (errorMessage) {
        }
    });
   }


  var ajaxArticle = function() {
      $.ajax({
        url: searchUrl,
        dataType: 'jsonp',
        data: {
          action: 'query',
          format: 'json',
          prop: 'extracts',
          exchars: '200',
          exlimit: 'max',
          explaintext: '',
          exintro: '',
          rawcontinue: '',
          generator: 'search',
          gsrsearch: toSearch,
          gsrnamespace: '0',
          gsrlimit: '10'
        }, //End data:
        success: function(json1) {
          console.log(json1);
        }
      }); //End .ajax()
    }

  //.ajax() to get images
  var ajaxImage = function() {
      $.ajax({
        url: searchUrl,
        dataType: 'jsonp',
        data: {
          'action': 'query',
          'titles': toSearch,
          'prop': 'pageimages',
          'format': 'json'
        }, //End data:
        success: function(json2) {
          console.log(json2)
        }
      }); //End .ajax()
    }

  //Auto complete search bar
  input.autocomplete({
    source: function(request, response) {
      $.ajax({
        url: searchUrl,
        dataType: 'jsonp',
        data: {
          'action': "opensearch",
          'format': "json",
          'search': request.term
        },
        success: function(data) {
          response(data[1]);
        }
      });
    }
  }); //End auto compelete

  //Listen for click on button to store search field
  //End click
})



</script>

</body>
</html>
"""


def artifact_list(request):
    artifacts = ArtifactDetail.objects.filter(artifact_no__contains="1").order_by('room_no')
    return render(request, 'details/artifact_list.html', {'artifacts':artifacts})



def search(request):
    if request.method == 'POST':
            srch = requests.POST('srh')
            if srch:
                match = ArtifactDetail.objects.filter(Q(artifact_name__icontains=srch) |
                                                    Q(artifact_description__icontains=srch)

                )
                if match:
                    return render(request,'details/search.html',{'sr':match})
                else:
                    messages.error(request,"no result found")

            else:
                return HttpResponseRedirect('/search/')
    return render(request,'details/search.html')

def room(request,i):
    artifacts = ArtifactDetail.objects.filter(room_no__contains=str(i))
    fila=open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates/details/'+"room_number"+str(i)+".html"),'w+')
    fila.write(room_template)
    fila.close()
    return render(request,'details/room_number'+str(i)+'.html',{'artifacts':artifacts})


def success(request):
    return render(request,'details/success.html')

def aravind(request):
    return render(request,'details/aravind.html')


from details.forms import FeedbackForm

def feedback(request):
    form_class = FeedbackForm
    return render(request,'details/feedbackform.html',{'form':form_class})
