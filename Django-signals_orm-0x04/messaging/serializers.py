from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Message, Conversation

class UserSerializer(ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'user_id', 'username', 'password',
            'confirm_password', 'first_name', 'last_name', 
            'email', 'phone_number', 'role', 'created_at',
            
            )

    

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('passwords do not match')
        return attrs
    def create(self, validated_data):
        validated_data.pop("confirm_password")
        instance = User.objects.create_user(**validated_data)
        return instance


    
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
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ('conversation_id', 'participants', 'created_at', 'messages')

    def get_messages(self, instance):
        messages = instance.messages
        return MessageSerializer(messages, many=True, read_only=True).data
    
    def create(self, validated_data):
        participants = validated_data.pop('participants', [])
        conversation = Conversation.objects.create(**validated_data)
        conversation.participants.set(participants)
        return conversation
    
    def update(self, instance, validated_data):
        new_participants = validated_data.pop('participants', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.participants.add(*new_participants)
        instance.save()

    
