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

    def get_userid(self):
        user_url = "https://api.vk.com/method/users.get"

        params_user = {
            'access_token': ACCESS_TOKEN,
            'v': '5.74',
            'user_ids': self.name 
        }
        try:
            response = requests.get(user_url, params = params_user)
            id = response.json()['response'][0]['id']
            return id
        except Exception:
            print('Неверно введен screen_name или id пользователя')
            
    def __repr__(self): 
        return f"{self}" 

    def __str__(self):
        try:
            int(self.name)
            return f"https://vk.com/id{self.name} "
        except Exception:
            return f"https://vk.com/{self.name} "

    def __and__(self, other):
        friends_params = {
        'access_token': ACCESS_TOKEN,
        'v': '5.74',
        'source_uid': self.get_userid(),
        'target_uid': other.get_userid(),
        }
        friends_url = "https://api.vk.com/method/friends.getMutual"
        try:
            response_mf = requests.get(friends_url, params = friends_params)
            mutual_friends = list(map(lambda x: 'id'+str(x), response_mf.json()['response']))
            mutual_friends = list(map(User, mutual_friends))
            return mutual_friends
        except Exception:
            print('Данные не введены, либо введены неверно')

             

if __name__ == "__main__":

    user1 = User(input('Введите screen_name или id пользователя: '))
    user2 = User(input('Введите screen_name или id пользователя: '))
    print(user1)
    print(user2)
    pprint(user1&user2)
    print(type((user1&user2)[0]))



