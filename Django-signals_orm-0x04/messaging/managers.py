
from django.db import models
class UnreadMessagesManager(models.Manager):
    def unread_messages(self):
        return self.get_queryset().filter(unread=True)
    
class UnreadMessageManagerQueryset(models.QuerySet):
    def unread_messages(self):
        return self.filter(unread=True)

class CustomUnreadMessageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(unread=True)
    
    def unread_for_user(self, user):
        return self.get_queryset().filter(receiver=user)