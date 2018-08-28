from django.template import loader
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .engine import *
from rest_framework.decorators import api_view
import random
from .forms import UploadFileForm
from .datahandler import *
from django.shortcuts import render


# Create your views here.

def search_bar(request):
    """
    View of the search bar page
    """
    pre_questions_list = Questions.objects.values('question')
    questions_list = random.sample(list(pre_questions_list), 1)
    template = loader.get_template('nluengine/search.html')
    context = {
        'question_hint': questions_list[0]
    }
    return HttpResponse(template.render(context, request))


@api_view(['POST'])
def nlu_engine(request, query):
    """
    End point where user request must arrive.
    :param request:
    :return:
    """
    if request.method == 'POST':
        clean_query = ''
        for character in query:
            if character == '+':
                clean_query += ' '
            else:
                clean_query += character
        response = resolve_query(clean_query)
        return JsonResponse(response)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if handle_data(request.FILES['file'], form.cleaned_data['field']):
                return HttpResponseRedirect('/engine/knowledge/')
        #     TODO handle error
        else:
            print("NO  Valido")
    else:
        form = UploadFileForm()
    return render(request, 'nluengine/upload.html', {'form': form})


def knowledge(request):
    """
    View knowledge JSON
    """
    template = loader.get_template('nluengine/knowledge.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


@api_view(['GET'])
def knowledge_api(request):
    """
    End point where knowledge data comes
    :param request:
    :return:
    """
    if request.method == 'GET':
        response = json.loads(get_training_data())
        return JsonResponse(response)
