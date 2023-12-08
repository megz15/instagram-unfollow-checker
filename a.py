from requests import get
from json import dump, load

with open('ids.json') as f:
    ids = load(f)
    user_id = ids["user_id"]
    session_id = ids["session_id"]

data = get(
    "https://i.instagram.com/api/v1/friendships/{}/followers".format(user_id), headers= {
        'user-agent':'Instagram 420.0.0.0.69'
    }, cookies= {
        'ds_user_id': user_id,
        'sessionid': session_id
    }).json()

# with open('followers.json', 'w') as f:
#     dump(data["users"], f)

print(data["users"])