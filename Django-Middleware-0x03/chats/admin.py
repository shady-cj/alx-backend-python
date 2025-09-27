from django.contrib import admin

# Register your models here.

from .models import User, Message, Conversation

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Conversation)