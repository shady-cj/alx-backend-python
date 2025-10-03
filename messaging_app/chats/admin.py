from django.contrib import admin

# Register your models here.

from .models import Message, User, Conversation, Notification


admin.site.register(Message)
admin.site.register(User)
admin.site.register(Conversation)
admin.site.register(Notification)