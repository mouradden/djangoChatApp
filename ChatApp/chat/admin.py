from django.contrib import admin
from chat.models import Chat


# Register your models here.

@admin.register(Chat)
class chatAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "receiver", "content")