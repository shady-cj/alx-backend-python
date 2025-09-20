from serializers import ModelSerializer, SerializerMethodField
from .models import User, Message, Conversation

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password_hash']

    
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

# class ConversationSerializer(ModelSerializer):
#     messages = MessageSerializer(many=True, read_only=True)
#     class Meta:
#         model = Conversation
#         fields = '__all__'


class ConversationSerializer(ModelSerializer):
    messages = SerializerMethodField(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('conversation_id', 'participants_id', 'created_at', 'messages')

    def get_messages(self, instance):
        messages = instance.messages
        return MessageSerializer(messages, many=True, read_only=True)