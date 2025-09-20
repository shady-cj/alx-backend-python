from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    ROLE = (
        ('GUEST', 'guest'),
        ('HOST', 'host'),
        ('ADMIN', 'admin')
    )
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(max_length=64, unique=True, null=False, blank=False, db_index=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=60, choices=ROLE, default=ROLE[0][0])
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sender_id = models.ForeignKey(User, related_name="messages", null=True, on_delete=models.SET_NULL)
    message_body = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    participants_id = models.ManyToManyField(User, related_name='conversations', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    messages = models.ManyToManyField(Message, related_name='conversation', null=True, blank=True)



