from django.shortcuts import render

# Create your views here.
from .models import Conversation, Message, User
from serializers import ConversationSerializer, MessageSerializer, UserSerializer

from rest_framework import viewsets, filters
from rest_framework.response import Response, status


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants_id__username', 'messages__message_body']

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body', 'sender_id__username']

    def get_queryset(self):
        return super().get_queryset().filter(conversation__conversation_id=self.kwargs['conversation_conversation_id']).distinct()



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']