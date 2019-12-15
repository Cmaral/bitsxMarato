from django.shortcuts import render
from django.http import HttpResponse
from diagnoser.api.request_handler import handle_params

class Question():
    #symptom_id: models.TextField()
    #symptom_def: models.TextField()
    #name = models.CharField(max_length=200)
    #synonyms = []

    def __init__(self, symptom_id, symptom_def, name):
        self.symptom_id = symptom_id
        self.symptom_def = symptom_def
        self.name = name
        self.synonyms = []

    def add_synonym(self, synonym):
        self.synonyms.append(synonym)



def index(request):
    symptom_ids = '' if request.GET.get('symptoms') is None else request.GET.get('symptoms')
    params = { 'symptoms' : symptom_ids }
    context = handle_params(params)

    #quest =  Question("1", "def", "nombre")
    #context = {}
    #return HttpResponse(context)

    return render(request,'index.html', context)



def default(request):
    return HttpResponse("default Page")

    return HttpResponse(
    f"""<!DOCTYPE html>

    <html lang="en">
      <head>
      <meta charset="utf-8">

      <title>Main Page</title>
      <meta name="description" content="The HTML5 Herald">
      <meta name="author" content="SitePoint">

      <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
      <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

      </head>
      <body>
        <div>
            <h1>question</h1>
            <p>{text_response['question']}</p>

        </div>
        <hr>
        <div>
            <h1>sintomas</h1>
                        <p>{text_response['symptoms']}</p>

        </div>
        <hr>
        <div>
            <h1>results</h1>
            <p>{text_response['results']}</p>

        </div>
        <hr>
      </body>
    </html>""")
    #return render(request, 'page.html')
# Create your views here.
