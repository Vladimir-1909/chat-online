from django.contrib import admin
from .models import Room, Chat


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_id", "user1", "user2", "date")


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("room", "user", "text", "date")