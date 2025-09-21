from django.shortcuts import render

# Create your views here.
from .models import Conversation, Message
from serializers import ConversationSerializer, MessageSerializer

from rest_framework import viewsets


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
