from .openvkapi import *


class messages:

    @staticmethod
    def send(client, user_id, message):
        response = http.get(f'https://openvk.su/method/Messages.send?user_id={user_id}&peer_id={-1}&message={message}&access_token={client}')
        return json.loads(response.text)['response']

    @staticmethod
    def delete(client, message_id):
        response = http.get(f'https://openvk.su/method/Messages.delete?messages_ids={message_id}&access_token={client}')
        return json.loads(response.text)

    @staticmethod
    def restore(client, message_id):
        response = http.get(f'https://openvk.su/method/Messages.restore?messages_ids={message_id}&access_token={client}')
        return json.loads(response.text)

    @staticmethod
    def get_conversations(client):
        response = http.get(f'https://openvk.su/method/Messages.getConversations?access_token={client}')
        return json.loads(response.text)['response']