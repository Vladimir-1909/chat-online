from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, verbose_name="user1", on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, verbose_name="user2", on_delete=models.CASCADE, related_name='user2')
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"


class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name="Комната чата", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"
