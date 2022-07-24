from openvkapi import *


class ovk:

    @staticmethod
    def version(client):
        return http.get(f'https://{client["instance"]}/method/Ovk.version?access_token={client["token"]}').json()

    @staticmethod
    def test(client):
        return http.get(f'https://{client["instance"]}/method/Ovk.test?access_token={client["token"]}').json()

    @staticmethod
    def chicken_wings(client):
        return http.get(f'https://{client["instance"]}/method/Ovk.chickenWings?access_token={client["token"]}').json()

    @staticmethod
    def about_instance(client):
        return http.get(f'https://{client["instance"]}/method/Ovk.aboutInstance?access_token={client["token"]}').json()
