from openvkapi import *


class messages:

    @staticmethod
    def send(client, user_id, message, peer_id=-1, domain='', chat_id=-1, user_ids='', sticker_id=-1):
        response = http.get(f'https://{client["instance"]}/method/Messages.send?user_id={user_id}&peer_id={peer_id}&message={message}%domain={domain}%chat_id={chat_id}&user_ids={user_ids}&sticker_id={sticker_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def delete(client, message_id):
        response = http.get(f'https://{client["instance"]}/method/Messages.delete?messages_ids={message_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def restore(client, message_id):
        response = http.get(f'https://{client["instance"]}/method/Messages.restore?messages_ids={message_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_conversations(client, offset=0, count=20, filter="all", extended=0):
        response = http.get(f'https://{client["instance"]}/method/Messages.getConversations?offset={offset}&count={count}&filter={filter}&extended={extended}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_history(client, user_id, offset=0, count=20, peer_id=-1, start_message_id=0, rev=0, extended=0):
        response = http.get(f'https://{client["instance"]}/method/Messages.getHistory?user_id={user_id}&offset={offset}&count={count}&peer_id={peer_id}&start_message_id={start_message_id}&rev={rev}&extended={extended}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_long_poll_history(client):
        response = http.get(f'https://{client["instance"]}/method/Messages.getLongPollHistory?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_long_poll_server(client):
        response = http.get(f'https://{client["instance"]}/method/Messages.getLongPollServer?access_token={client["token"]}')
        return json.loads(response.text)