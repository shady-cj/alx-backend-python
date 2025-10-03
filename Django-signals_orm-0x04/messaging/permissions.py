from rest_framework import permissions
from .models import Conversation

class IsParticipantOfConversation(permissions.BasePermission):
    def has_permission(self, request, view):
        from .views import ConversationViewSet

        #  ["PUT", "PATCH", "DELETE"]
        if not request.user or not request.user.is_authenticated:
            return False
        
        if isinstance(view, ConversationViewSet):
            conversation_pk = view.kwargs.get('pk')
        else:
            conversation_pk = view.kwargs.get("conversation_pk")
    
        if conversation_pk:
            conversation = Conversation.objects.get(conversation_id = conversation_pk)
            print(conversation.participants_id.contains(request.user))
            return conversation.participants_id.contains(request.user)
        return True
    