import requests as http


class openvkapi:

    @staticmethod
    def auth(login='', password='', code=0, instance='openvk.su', token=''):
        if token == '':
            response = http.get(f'https://{instance}/token?username={login}&password={password}&code={code}&grant_type=password').json()
            token = str(response['access_token'])
            user_id = int(response['user_id'])
            response = {
                'instance': instance,
                'token': token,
                'id': user_id
            }
            return response
        elif token != '':
            response = {
                'instance': instance,
                'token': token
            }
            return response

    @staticmethod
    def pam():
        print('Вы потрогали Утинку за ляшки через Api')
