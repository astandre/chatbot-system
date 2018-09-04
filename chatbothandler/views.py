from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .services import get_intent


# Create your views here.
@api_view(['POST'])
def new_user(request):
    """
    End point where new user is registered
    :param request:
    :return:
    """
    if request.method == 'POST':
        serializer = SocialNetworksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 201}, status=status.HTTP_201_CREATED)
        return Response({"status": 400}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def new_input(request):
    """
    End point where new input is registered and analyzed
    :param request:
    :return:
    """
    if request.method == 'POST':
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            input_name = Inputs.objects.values('id_input').last()
            # TODO resolve intent
            # Entry.objects.filter(pub_date__year=2010).update(comments_on=False)
            # intent = get_intent(serializer.validated_data["text"])
            print(input_name)
            return Response({"status": 201}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
