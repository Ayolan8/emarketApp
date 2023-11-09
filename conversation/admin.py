from django.contrib import admin
from .models import Conversation, ConversationMesssage

admin.site.register(Conversation)
admin.site.register(ConversationMesssage)
