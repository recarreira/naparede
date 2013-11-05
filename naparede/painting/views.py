from django.shortcuts import render_to_response
from models import Painting
from models import Galery

def home(request):
    paintings = Painting.objects.all()
    galeries = Galery.objects.all()
    return render_to_response('index.html', {
        "paintings": paintings,
        "galeries": galeries,
        })