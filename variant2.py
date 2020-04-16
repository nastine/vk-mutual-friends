from urllib.parse import urlencode
import requests
from pprint import pprint

APP_ID = 7410959
AUTH_URL = "https://oauth.vk.com/authorize"
AUTH_PARAM = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends, status, wall, groups, stats, offline',
    'response_type': 'token',
    'v': '5.74'
}
# print('?'.join((AUTH_URL, urlencode(AUTH_PARAM))))

ACCESS_TOKEN ='0639aef390b41e4f1c8eb0aca689bc93e7289edb19ab158d99fa4e2c5c241780269cf666d76a566bbb454'

class User:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        user_id = self.get_userid()
        return f'https://vk.com/id{user_id}'

    def __and__(self, other):
        try:
            target_uid = other.get_userid()
            mutual_list = self.get_mutual_friends(target_uid)
            mutual_list = list(map(lambda x: User(x), mutual_list))
            return mutual_list
        except Exception:
            print("Данные не введены, либо введены неверно")

    def get_userid(self):
        
        URL = 'https://api.vk.com/method/users.get'
        params = {
            'user_ids': self.name,
            'access_token': ACCESS_TOKEN,
            'v': '5.52'
        }
        try:
            response = requests.get(URL, params=params)
            user_id = response.json()['response'][0]['id']
            return user_id
        except Exception:
            print("Неверно введен screen_name или id пользователя")

    def get_mutual_friends(self, target_uid):
        URL = 'https://api.vk.com/method/friends.getMutual'
        params = {
            'source_uid': self.get_userid(),
            'target_uid': target_uid,
            'access_token': ACCESS_TOKEN,
            'v': '5.52'
        }
        response = requests.get(URL, params=params)
        mutual_list = response.json()['response']
        return mutual_list


if __name__ == "__main__":

    user1 = User(input('Введите screen_name или id пользователя: '))
    user2 = User(input('Введите screen_name или id пользователя: '))
    print(user1)
    print(user2)
    pprint(user1&user2)
    print(type((user1&user2)[0]))
