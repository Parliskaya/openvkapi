from openvkapi import *


class ovk:

    @staticmethod
    def version(client):
        response = http.get(f'https://{client["instance"]}/method/Ovk.version?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def test(client):
        response = http.get(f'https://{client["instance"]}/method/Ovk.test?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def chicken_wings(client):
        response = http.get(f'https://{client["instance"]}/method/Ovk.chickenWings?access_token={client["token"]}')
        return json.loads(response.text)

    @staticmethod
    def about_instance(client):
        response = http.get(f'https://{client["instance"]}/method/Ovk.aboutInstance?access_token={client["token"]}')
        return json.loads(response.text)