from openvkapi import *


class likes:

    @staticmethod
    def add(client, type, owner_id, item_id):
        response = http.get(f'https://{client["domen"]}/method/Likes.add?type={type}&owner_id={owner_id}&item_id={item_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def remove(client, type, owner_id, item_id):
        response = http.get(f'https://{client["domen"]}/method/Likes.remove?type={type}&owner_id={owner_id}&item_id={item_id}&access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def is_liked(client, user_id, type, owner_id, item_id):
        response = http.get(f'https://{client["domen"]}/method/Likes.remove?user_id={user_id}&type={type}&owner_id={owner_id}&item_id={item_id}&access_token={client["token"]}')
        return json.loads(response.text)