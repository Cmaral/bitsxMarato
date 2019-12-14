from django.shortcuts import render
from django.http import HttpResponse
from api.request_handler import handle_params

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

text_response= {
    question='default_question_text',
    symptoms='default_symptoms_text',
    results='default_results_text'
}

def default(request):
    symptom_ids = '' if request.GET.get('symptoms') is None else request.GET.get('symptoms')
    params['symptoms'] = symptom_ids
    text_response = handle_params(params)
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
