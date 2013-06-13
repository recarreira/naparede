from django.shortcuts import render_to_response
from models import Painting


def home(request):
    #import pdb; pdb.set_trace()
    return render_to_response('index.html', {
        "paintings": Painting.objects.all(),
        })