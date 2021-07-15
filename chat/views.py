from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . import models
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.user.is_anonymous:
        return redirect('user')

    search_query = request.GET.get('search', '')
    users = None
    if search_query:
        user1 = models.Room.objects.filter(user1=request.user)
        user2 = models.Room.objects.filter(user2=request.user)
        if user1:
            user2_id = []
            for item in user1:
                user2_id.append(item.user2.id)
            user2_id.append(request.user.id)
            users = User.objects.filter(username__icontains=search_query).exclude(id__in=user2_id)
        elif user2:
            user1_id = []
            for item in user2:
                user1_id.append(item.user1.id)
            user1_id.append(request.user.id)
            users = User.objects.filter(username__icontains=search_query).exclude(id__in=user1_id)
        else:
            users = User.objects.filter(username__icontains=search_query).exclude(id=request.user.id)
        if not users:
            messages.success(request, f'Такой "@{search_query}" никнейм не существует!')

    user1 = models.Room.objects.filter(user1=request.user)
    user2 = models.Room.objects.filter(user2=request.user)

    data = {
        'users': users,
        'rooms': user1,
        'roomss': user2,
    }
    return render(request, 'chat/home.html', data)


def add_room(request, user_id):
    if request.user.is_anonymous:
        return redirect('user')

    user1 = request.user
    user2 = User.objects.filter(id=user_id).first()
    rooms = models.Room()
    rooms.user1 = user1
    rooms.user2 = user2
    rooms.save()
    return redirect('home')


def room(request, room_name):
    if request.user.is_anonymous:
        return redirect('user')

    """"""
    user1 = models.Room.objects.filter(user1=request.user)
    user2 = models.Room.objects.filter(user2=request.user)
    room = models.Room.objects.filter(room_id=room_name).first()
    chats = models.Chat.objects.filter(room=room)
    return render(request, 'chat/room.html', {
        'chats': chats,
        'rooms': user1,
        'roomss': user2,
        'room': room
    })


def save_message(request):
    if request.user.is_anonymous:
        return redirect('user')

    room = request.POST.get('room', '')
    text = request.POST.get('text', '')
    room_qs = models.Room.objects.filter(room_id=room).first()
    chat = models.Chat()
    chat.user = request.user
    chat.room = room_qs
    chat.text = text
    chat.save()
    return redirect(f'/{room}/')


def remove_message(request, pid):
    if not pid:
        return HttpResponse("Not pid")

    chat = models.Chat.objects.filter(id=pid).first()
    chat.delete()
    return HttpResponse('Ok')
