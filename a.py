from requests import get
from json import dump, load

with open('ids.json') as f:
    ids = load(f)
    user_id = ids["user_id"]
    session_id = ids["session_id"]

max_id = ''
users = {}

def get_users(user_id, session_id, group = "following", count = 200, max_id = '', batch_no = 1):
    data = get(
        f"https://i.instagram.com/api/v1/friendships/{user_id}/{group}?count={count}&max_id={max_id}", headers= {
            'user-agent':'Instagram 420.0.0.0.69'
        }, cookies= {
            'ds_user_id': user_id,
            'sessionid': session_id
        }).json()

    try:
        max_id = data["next_max_id"]
        print(f"[🦕] Got {batch_no} batch of {group}, getting the next...")
        get_users(user_id, session_id, group, count, max_id, batch_no + 1)
    except KeyError:
        print("[🐍] Got all {} {}!".format((batch_no - 1) * count + len(data["users"]), group))
        return

    for i in data["users"]:
        if i["pk"] not in users:
            users[len(users)] = {
                "id": i["pk"],
                "username": i["username"],
                "name": i["full_name"],
                "pfp": i["profile_pic_url"],
                "is_private": i["is_private"]
            }

get_users(user_id, session_id, "following", 200)

with open('following.json', 'w') as f:
    dump(users, f)
    users.clear()

get_users(user_id, session_id, "followers", 24)

with open('followers.json', 'w') as f:
    dump(users, f)
    users.clear()