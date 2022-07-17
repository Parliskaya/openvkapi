from openvkapi import *


class friends:

    @staticmethod
    def get(client, user_id, fields='', offset=0, count=100):
        response = http.get(f'https://{client["instance"]}/method/Friends.get?user_id={user_id}&fields={fields}&offset={offset}&count={count}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def add(client, user_id):
        response = http.get(f'https://{client["instance"]}/method/Friends.add?user_id={user_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def remove(client, user_id):
        response = http.get(f'https://{client["instance"]}/method/Friends.remove?user_id={user_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def get_list(client):
        response = http.get(f'https://{client["instance"]}/method/Friends.getLists?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def list(client, value):
        if value == 0:
            response = http.get(f'https://{client["instance"]}/method/Friends.edit?access_token={client["token"]}')
            return json.loads(response.text)

        elif value == 1:
            response = http.get(f'https://{client["instance"]}/method/Friends.deleteList?access_token={client["token"]}')
            return json.loads(response.text)

        elif value == 2:
            response = http.get(f'https://{client["instance"]}/method/Friends.editList?access_token={client["token"]}')
            return json.loads(response.text)

        else:
            pass
