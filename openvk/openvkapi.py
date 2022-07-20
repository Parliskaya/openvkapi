import requests as http
import json


class openvkapi:

    """Авторизация пользователя"""

    @staticmethod
    def auth(login: str, password: str, instance='openvk.su', code=0):
        response = http.get(f'https://{instance}/token?username={login}&password={password}&code={code}&grant_type=password')
        token = str(json.loads(response.text)['access_token'])
        user_id = int(json.loads(response.text)['user_id'])
        response = {
            'instance': instance,
            'token': token,
            'id': user_id
        }
        return response

    @staticmethod
    def pam():
        print('Вы потрогали Утинку за ляшки через Api')
