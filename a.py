from requests import get
from json import dump, load

with open('ids.json') as f:
    ids = load(f)
    user_id = ids["user_id"]
    session_id = ids["session_id"]

batch_no = 1
max_id = ''
users = {}

while True:
    data = get(
        "https://i.instagram.com/api/v1/friendships/{}/followers?max_id={}".format(user_id, max_id), headers= {
            'user-agent':'Instagram 420.0.0.0.69'
        }, cookies= {
            'ds_user_id': user_id,
            'sessionid': session_id
        }).json()

    try:
        max_id = data["next_max_id"]
        print(f"[🦕] Got {batch_no} batch of users, getting the next...")
        batch_no += 1
    except KeyError:
        print(f"[🐍] Got all {len(users)} users!")
        break

    for i in data["users"]:
        if i["pk"] not in users:
            users[len(users)] = {
                "id": i["pk"],
                "username": i["username"],
                "name": i["full_name"],
                "pfp": i["profile_pic_url"],
                "is_private": i["is_private"]
            }

with open('followers.json', 'w') as f:
    dump(data["users"], f)

# print(users)