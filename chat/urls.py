from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save_message/', views.save_message, name='save_message'),
    path('remove/<int:pid>/', views.remove_message, name='remove_message'),
    path('<str:room_name>/', views.room, name='room'),
    path('user/<int:user_id>/', views.add_room, name='add_room'),

]
