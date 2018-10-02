from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .intent_handler import *


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
            last_input_id = Inputs.objects.values('id_input').last()
            if "intent" not in serializer.validated_data:
                intent = get_intent(serializer.validated_data["text"])
                intent["context"] = serializer.validated_data["context"]
            else:
                intent = {
                    "intent": serializer.validated_data["intent"],
                    "context": serializer.validated_data["context"]
                }
            print("ENTRY DATA IH >>> ", intent)
            if intent["intent"] is not None:
                intent = intent_handler(intent)
                intent_answer = Intents.objects.get(name=intent["intent"])
                Inputs.objects.filter(id_input=last_input_id["id_input"]).update(
                    intent=intent_answer, solved=True)
            return Response(intent, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
