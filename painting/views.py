from django.shortcuts import render_to_response
from models import Painting


def home(request):
    paintings = Painting.objects.all()
    return render_to_response('index.html', {
        "paintings": paintings,
        })