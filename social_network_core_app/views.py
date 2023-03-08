from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .chats_model import ChatRoom, Message
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
# Create your views here.

@login_required
def profile(request):
    return render(request, 'social_network_core_app/profile.html')

@login_required
def chat_room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    messages = Message.objects.filter(room=room)
    context = {'room': room, 'messages': messages}
    return render(request, 'social_network_core_app/room.html', context)

@login_required
def message_create(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')


