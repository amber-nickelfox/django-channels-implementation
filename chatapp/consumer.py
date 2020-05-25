import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    """
    This is a synchronous WebSocket consumer that accepts
    all connections, receives messages from its client, and echos
    those messages back to the same client. For now it does not
    broadcast messages to other clients in the same room.
    """

    def connect(self):
        """
        connect
        :return:
        """
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        """
        Receive data
        :param text_data:
        :param bytes_data:
        :return:
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps(
            {
                'message': message
            }
        ))
