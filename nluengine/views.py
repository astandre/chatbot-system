from django.template import loader
from django.http import HttpResponse, JsonResponse
from .engine import *
from rest_framework.decorators import api_view
import random


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
