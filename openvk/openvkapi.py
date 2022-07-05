import requests as http
import json


class openvkapi:

    """Авторизация пользователя"""

    @staticmethod
    def auth(login: str, password: str):
        response = http.get(f'https://openvk.su/token?username={login}&password={password}&grant_type=password')
        token = str(json.loads(response.text)['access_token'])
        return token
