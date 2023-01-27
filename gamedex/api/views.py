from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Games
from .serializers import *

@api_view(['GET'])
def games_list(request):
    if request.method == 'GET':
        data = Games.objects.all()
        serializer = GameSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)