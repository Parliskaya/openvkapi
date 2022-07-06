from openvkapi import *


class friends:

    @staticmethod
    def get(client, user_id):
        response = http.get(f'https://{client["domen"]}/method/Friends.get?user_id={user_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def add(client, user_id):
        response = http.get(f'https://{client["domen"]}/method/Friends.add?user_id={user_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def remove(client, user_id):
        response = http.get(f'https://{client["domen"]}/method/Friends.remove?user_id={user_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_list(client):
        response = http.get(f'https://{client["domen"]}/method/Friends.getLists?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def list(client, value):
        if value == 0:
            response = http.get(f'https://{client["domen"]}/method/Friends.edit?access_token={client["token"]}')
            return json.loads(response.text)

        elif value == 1:
            response = http.get(f'https://{client["domen"]}/method/Friends.deleteList?access_token={client["token"]}')
            return json.loads(response.text)

        elif value == 2:
            response = http.get(f'https://{client["domen"]}/method/Friends.editList?access_token={client["token"]}')
            return json.loads(response.text)

        else:
            pass
