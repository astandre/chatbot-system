from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Intents, Questions, Entities
from .engine import *
import json


# Create your views here.

def nlu_engine(request):
    """
    View of the main page
    """


    data = getTrainingData()
    # print(data)
    # print(type(data))
    # data_json = json.loads(data)
    # print(data_json)
    template = loader.get_template('nluengine/search.html')
    context = {
        'data': data,
    }
    return HttpResponse(template.render(context, request))
