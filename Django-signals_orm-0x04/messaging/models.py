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
    sender = models.ForeignKey(User, related_name="sent_messages", null=True, on_delete=models.SET_NULL)
    receiver = models.ForeignKey(User, related_name = "received_messages", null=True, on_delete=models.SET_NULL)
    edited = models.BooleanField(default=False)
    content = models.TextField(null=False, blank=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class MessageHistory(models.Model):
    history_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    message = models.ForeignKey(Message, related_name="histories", null=True, on_delete=models.CASCADE)
    old_content = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    participants = models.ManyToManyField(User, related_name='conversations', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    messages = models.ManyToManyField(Message, related_name='conversation', blank=True)
    class Meta:
        ordering = ['-created_at']


class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    message = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, related_name='notifications', null=True, on_delete=models.SET_NULL)
    is_read = models.BooleanField(default=False)

