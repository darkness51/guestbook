from django.contrib import admin
from main.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ["email", "date"]

admin.site.register(Message, MessageAdmin)