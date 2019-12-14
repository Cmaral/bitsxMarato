from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

question_text='duck'
sintomas_text='duck2'
results_text='duck3'

def default(request):
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
            <p>{question_text}</p>

        </div>
        <hr>
        <div>
            <h1>sintomas</h1>
                        <p>{sintomas_text}</p>

        </div>
        <hr>
        <div>
            <h1>results</h1>
            <p>{results_text}</p>

        </div>
        <hr>
      </body>
    </html>""")
    #return render(request, 'page.html')
# Create your views here.
