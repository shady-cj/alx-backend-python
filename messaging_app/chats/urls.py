from rest_framework import routers
from rest_framework_nested import NestedDefaultRouter
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet, UserViewSet

router = routers.DefaultRouter()


router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')

conversation_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversation_router.urls)),
]
