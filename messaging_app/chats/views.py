from django.shortcuts import render

# Create your views here.
from .models import Conversation, Message
from serializers import ConversationSerializer, MessageSerializer

from rest_framework import viewsets
from rest_framework.response import Response, status


class ConversationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Conversation.objects.all()
        serializer = ConversationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MessageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
