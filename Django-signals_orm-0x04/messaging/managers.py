
from django.db import models
class UnreadMessagesManager(models.Manager):
    def unread_messages(self):
        return self.get_queryset().filter(unread=True)
    
class UnreadMessageManagerQueryset(models.QuerySet):
    def unread_messages(self):
        return self.filter(unread=True)