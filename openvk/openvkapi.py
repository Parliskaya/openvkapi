import requests as http
import json


class openvkapi:

    """Авторизация пользователя"""

    @staticmethod
    def auth(login: str, password: str, domen='openvk.su'):
        response = http.get(f'https://openvk.su/token?username={login}&password={password}&grant_type=password')
        token = str(json.loads(response.text)['access_token'])
        user_id = int(json.loads(response.text)['user_id'])
        response = {
            'domen': domen,
            'token': token,
            'id': user_id
        }
        return response
