
from django.db import models
class UnreadMessagesManager(models.Manager):
    def unread_messages(self):
        return self.get_queryset().filter(read=False)
    
class UnreadMessageManagerQueryset(models.QuerySet):
    def unread_messages(self):
        return self.filter(read=False)