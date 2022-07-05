from .openvkapi import *


class messages:

    def __init__(self):
        self.client = None
        self.response = None

    def send(self, client, user_id, message):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Messages.send?user_id={user_id}&peer_id={-1}&message={message}&access_token={self.client}')
        return json.loads(self.response.text)['response']

    def delete(self, client, message_id):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Messages.delete?messages_ids={message_id}&access_token={self.client}')
        return json.loads(self.response.text)

    def restore(self, client, message_id):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Messages.restore?messages_ids={message_id}&access_token={self.client}')
        return json.loads(self.response.text)

    def get_conversations(self, client):
        self.client = client
        self.response = http.get(f'https://openvk.su/method/Messages.getConversations?access_token={self.client}')
        return json.loads(self.response.text)['response']