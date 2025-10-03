from django.shortcuts import render

# Create your views here.
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer

from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter
from .pagination import CustomPagination


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [IsParticipantOfConversation]
    search_fields = ['participants__username', 'messages__content']
    filterset_fields = ["participants"]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['content', 'sender__username', 'receiver__username']
    filterset_class = MessageFilter
    permission_classes = [IsParticipantOfConversation]
    pagination_class = CustomPagination

    def get_queryset(self):
        # Message.objects.filter()
        # raise HTTP_403_FORBIDDEN if not permitted
        user = self.request.user
        return Message.objects.select_related('sender', 'receiver').prefetch_related('replies').filter(conversation__conversation_id=self.kwargs['conversation_pk'], conversation__participants=user.user_id).distinct()
    
    def perform_create(self, serializer):
        conversation_pk = self.kwargs.get('conversation_pk')
        conversation = Conversation.objects.get(conversation_id=conversation_pk)
        request = self.request
        instance = serializer.save(sender=request.user)
        conversation.messages.add(instance)
         # Notify other participants
        return instance



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']


    # handles delete_user 
    # user.delete()
    # 

    def get_permissions(self):
        if self.request.method == "POST" and 'pk' not in self.kwargs:
            # Allow registration of new users
            self.permission_classes = [permissions.AllowAny]
        
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in self.permission_classes]