from openvkapi import *


class friends:

    @staticmethod
    def get(client, user_id, fields='', offset=0, count=100):
        return http.get(f'https://{client["instance"]}/method/Friends.get?user_id={user_id}&fields={fields}&offset={offset}&count={count}&access_token={client["token"]}').json()

    @staticmethod
    def add(client, user_id):
        return http.get(f'https://{client["instance"]}/method/Friends.add?user_id={user_id}&access_token={client["token"]}').json()

    @staticmethod
    def remove(client, user_id):
        return http.get(f'https://{client["instance"]}/method/Friends.remove?user_id={user_id}&access_token={client["token"]}').json()

    @staticmethod
    def get_list(client):
        return http.get(f'https://{client["instance"]}/method/Friends.getLists?access_token={client["token"]}').json()

    @staticmethod
    def list(client, value):
        if value == 0:
            return http.get(f'https://{client["instance"]}/method/Friends.edit?access_token={client["token"]}').json()
        elif value == 1:
            return http.get(f'https://{client["instance"]}/method/Friends.deleteList?access_token={client["token"]}').json()
        elif value == 2:
            return http.get(f'https://{client["instance"]}/method/Friends.editList?access_token={client["token"]}').json()
        else:
            pass
