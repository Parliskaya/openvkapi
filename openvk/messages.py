from openvkapi import *


class messages:

    @staticmethod
    def send(client, user_id, message):
        response = http.get(f'https://{client["domen"]}/method/Messages.send?user_id={user_id}&peer_id={-1}&message={message}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def delete(client, message_id):
        response = http.get(f'https://{client["domen"]}/method/Messages.delete?messages_ids={message_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def restore(client, message_id):
        response = http.get(f'https://{client["domen"]}/method/Messages.restore?messages_ids={message_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_conversations(client):
        response = http.get(f'https://{client["domen"]}/method/Messages.getConversations?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_history(client):
        response = http.get(f'https://{client["domen"]}/method/Messages.getHistory?access_token={client["token"]}')
        return 'Разработчики ОпенВк пока что не сделали чаты, с днём завтра маслёнок'
        # return json.loads(response.text)

    @staticmethod
    def get_long_poll_history(client):
        response = http.get(f'https://{client["domen"]}/method/Messages.getLongPollHistory?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_long_poll_server(client):
        response = http.get(f'https://{client["domen"]}/method/Messages.getLongPollServer?access_token={client["token"]}')
        return json.loads(response.text)