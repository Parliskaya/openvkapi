from openvkapi import *


class groups:

    @staticmethod
    def get(client, user_id):
        response = http.get(f'https://{client["domen"]}/method/Groups.get?user_id={user_id}&access_token={client["token"]}')
        return json.loads(response.text)