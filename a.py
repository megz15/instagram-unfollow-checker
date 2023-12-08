from requests import get
from json import dump, load

with open('ids.json') as f:
    ids = load(f)
    user_id = ids["user_id"]
    session_id = ids["session_id"]

users = {}

data = get(
    "https://i.instagram.com/api/v1/friendships/{}/followers".format(user_id), headers= {
        'user-agent':'Instagram 420.0.0.0.69'
    }, cookies= {
        'ds_user_id': user_id,
        'sessionid': session_id
    }).json()

for i in data["users"]:
    if i["pk"] not in users:
        users[len(users)] = {
            "id": i["pk"],
            "username": i["username"],
            "name": i["full_name"],
            "pfp": i["profile_pic_url"],
            "is_private": i["is_private"]
        }

# with open('followers.json', 'w') as f:
#     dump(data["users"], f)

print(users)