from django.shortcuts import render

# Create your views here.
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer

from rest_framework import viewsets, filters, permissions
from rest_framework import status
from .permissions import IsParticipantOfConversation

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsParticipantOfConversation]
    search_fields = ['participants_id__username', 'messages__message_body']

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body', 'sender_id__username']
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        # Message.objects.filter()
        # raise HTTP_403_FORBIDDEN if not permitted
        user = self.request.user
        return super().get_queryset().filter(conversation__conversation_id=self.kwargs['conversation_pk'], conversation__participants_id=user.user_id).distinct()



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']

    def get_permissions(self):
        if self.request.method == "POST" and 'pk' not in self.kwargs:
            # Allow registration of new users
            self.permission_classes = [permissions.AllowAny]
        
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in self.permission_classes]