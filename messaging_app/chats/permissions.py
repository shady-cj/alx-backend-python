from rest_framework import permissions
from .models import Conversation

class MessageConversationPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        conversation_pk = view.kwargs["conversation_pk"]
        conversation = Conversation.objects.get(conversation_id = conversation_pk)
        return conversation.participants_id.contains(request.user)