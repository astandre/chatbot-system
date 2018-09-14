from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .services import get_intent, generate_answer


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
            # TODO get type of entity
            if "expected_intent" in serializer.validated_data:
                correct_intent = Intents.objects.values("name", "answer").get(
                    id_intent=serializer.validated_data["expected_intent"])
                intent = {"intent": correct_intent["name"],
                          "slots": [{"entity": "custom", "value": serializer.validated_data["text"]
                                     }], "answer": correct_intent["answer"]}
            else:
                intent = get_intent(serializer.validated_data["text"])
            if intent["intent"] is not None:
                intent = generate_answer(intent)
                intent_answer = Intents.objects.get(name=intent["intent"])
                Inputs.objects.filter(id_input=last_input_id["id_input"]).update(
                    intent=intent_answer, solved=True)
            return Response(intent, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
