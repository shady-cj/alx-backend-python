from serializers import ModelSerializer
from .models import User, Message, Conversation

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password_hash']

    
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ConversationSerializer(ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        fields = '__all__'
