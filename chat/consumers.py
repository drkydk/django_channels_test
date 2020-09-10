import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Channel
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        session_key = self.scope['session'].session_key
        connector = self.scope['cookies']['sessionid']
        connected_to = self.room_name.replace(session_key, '')

        if session_key == connector:
            await self.update_message_status_on_connect(connector, connected_to)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = self.scope['cookies']['sessionid']
        session_key = self.scope['session'].session_key
        recipient = self.room_name.replace(sender, '')

        if session_key == sender:
            print('OK')
            await self.log_message(sender, recipient, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': sender[:4] + ': ' + message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        sender = self.scope['cookies']['sessionid']
        session_key = self.scope['session'].session_key
        recipient = self.room_name.replace(sender, '')

        if session_key == recipient:
            Message.objects.filter(sender=sender, recipient=recipient).update(seen=True)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def update_message_status_on_connect(self, connector, connected_to):
        Message.objects.filter(sender=connected_to, recipient=connector).update(seen=True)
        channel = Channel.objects.get_or_create(room_name=self.room_name)[0]
        channel.seen_by = channel.seen_by.replace(connector, '') + connector
        channel.save()

    @database_sync_to_async
    def log_message(self, sender, recipient, message):
        print('IN')
        channel = Channel.objects.get_or_create(room_name=self.room_name)[0]
        log_data = {'room': channel,
                    'content': message,
                    'sender': sender,
                    "recipient": recipient}
        Message.objects.create(**log_data)
        channel.seen_by = sender
        channel.save()
        print('DONE!')
