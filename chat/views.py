from django.shortcuts import render
from rest_framework.views import APIView
from .models import Message


class ChatAPI(APIView):

    def get(self, request):
        return render(request, 'chat/index.html')


def room(request, room_name):
    session_id = request.session.session_key

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user_name': session_id,
        'session_id': session_id,
        'messages': Message.objects.filter(room__room_name=room_name).order_by('timestamp')
    })
