from django.contrib import admin
from .models import *

class InboxMessageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'conversation', 'brief_text', )
    readonly_fields = ('sender', 'conversation', 'body')


admin.site.register(InboxMessage, InboxMessageAdmin)
admin.site.register(Conversation)
