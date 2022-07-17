from openvkapi import *


class likes:

    @staticmethod
    def add(client, owner_id, item_id):
        response = http.get(f'https://{client["instance"]}/method/Likes.add?type=post&owner_id={owner_id}&item_id={item_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def remove(client, owner_id, item_id):
        response = http.get(f'https://{client["instance"]}/method/Likes.remove?type=post&owner_id={owner_id}&item_id={item_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def is_liked(client, user_id, owner_id, item_id):
        response = http.get(f'https://{client["instance"]}/method/Likes.remove?user_id={user_id}&type=post&owner_id={owner_id}&item_id={item_id}&access_token={client["token"]}')
        return json.loads(response.text)