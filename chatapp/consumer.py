import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    """
    This is a synchronous WebSocket consumer that accepts
    all connections, receives messages from its client, and echos
    those messages back to the same client. For now it does not
    broadcast messages to other clients in the same room.
    """

    def connect(self):
        """
        self.scope['url_route']['kwargs']['room_name']
        1. Obtains the 'room_name' parameter from the
        URL route in chat/routing.py that opened the WebSocket
        connection to the consumer.
        2. Every consumer has a scope that contains information
        about its connection, including in particular any positional
        or keyword arguments from the URL route and the currently
        authenticated user if any.
        ========================================================
        self.room_group_name = 'chat_%s' % self.room_name
        1. Constructs a Channels group name directly from the user-specified room name, without any quoting or escaping.
        2. Group names may only contain letters, digits, hyphens, and periods. Therefore this example code will fail on
        room names that have other characters.
        ========================================================
        async_to_sync(self.channel_layer.group_add)(...)
        1. Joins a group.
        2. The async_to_sync(…) wrapper is required because ChatConsumer is a synchronous WebsocketConsumer but it is
        calling an asynchronous channel layer method. (All channel layer methods are asynchronous.)
        3. Group names are restricted to ASCII alphanumerics, hyphens, and periods only. Since this code constructs a
        group name directly from the room name, it will fail if the room name contains any characters that aren’t valid
        in a group name.
        ========================================================
        self.accept()
        1. Accepts the WebSocket connection.
        2. If you do not call accept() within the connect() method then the connection will be rejected and closed.
        You might want to reject a connection for example because the requesting user is not authorized to perform the
        requested action.
        3. It is recommended that accept() be called as the last action in connect() if you choose to accept the
        connection.
        :return:
        """
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        """
        Leave group
        :param code:
        :return:
        """
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        """
        async_to_sync(self.channel_layer.group_send)
        1. Sends an event to a group.
        2. An event has a special 'type' key corresponding to the name of the method that should be invoked on consumers
        that receive the event.
        :param text_data:
        :param bytes_data:
        :return:
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(
            {
                'message': message
            }
        ))
