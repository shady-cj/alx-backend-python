
# Register your models here.
from django.contrib import admin

from .models import Message, User, Conversation, Notification


admin.site.register(Message)
admin.site.register(User)
admin.site.register(Conversation)
admin.site.register(Notification)