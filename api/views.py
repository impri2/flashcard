import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import CardSerializer,CardGetSerializer,AnswerSerializer,SettingSerializer,ImageSerializer
from .models import Card,Settings
# Create your views here.
@api_view(['POST'])
def add_card(request):
    serializer =  CardGetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def all_cards(request):
    cards = Card.objects.all()
    serializer = CardGetSerializer(cards,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_card(request,pk):
    card = Card.objects.get(id=pk)
    card.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def today_cards(request):
    new_max_card = Settings.objects.get(id=1).questions_per_day
    cards = Card.objects.all()
    today_card = []
    new_card = []
    today = datetime.datetime.now().date()
    for card in cards:
        if (today - card.last_learned).days >= card.interval:
            if card.last_learned.year >= 2000:
                today_card.append(card)
            else:
                if len(new_card) < new_max_card:
                    new_card.append(card)
    today_card += new_card
    serializer = CardGetSerializer(today_card,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def answer_card(request):
    print(request.data)
    serializer =  AnswerSerializer(data=request.data)
    serializer.is_valid()
    id = request.data['id']
    correct = request.data['correct']
    card = Card.objects.get(pk=id)
    card.last_learned = datetime.datetime.now().date()
    card.interval = card.interval + 2 if correct else 1
    card.save()
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def get_settings(request):
    setting = Settings.objects.get(pk=1)
    serializer = SettingSerializer(setting)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def set_settings(request):
    setting = Settings.objects.get(pk=1)
    serializer = SettingSerializer(data=request.data)
    serializer.is_valid()
    setting.study_time = serializer.validated_data['study_time']
    setting.questions_per_day = serializer.validated_data['questions_per_day']
    setting.save()
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def should_study(request):
    study_time = Settings.objects.get(id=1).study_time
    cards = Card.objects.all()
    time = datetime.datetime.now().time()
    date = datetime.datetime.now().date()
    for card in cards:
        if card.last_learned == date:
            return Response({'study':False},status=status.HTTP_200_OK)

    return Response({'study':time > study_time},status=status.HTTP_200_OK)
    
    
