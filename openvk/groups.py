from openvkapi import *


class groups:

    @staticmethod
    def get(client, user_id, fields='', offset=0, count=100):
        response = http.get(f'https://{client["instance"]}/method/Groups.get?user_id={user_id}&fields={fields}&offset={offset}&count={count}&access_token={client["token"]}')
        return json.loads(response.text)