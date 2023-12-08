# Instagram Unfollow Checker

This script uses the Instagram web API to check discrepancies between the users you follow and the users that follow you. I got to know that people send follow requests and unfollow you later to boost their ✨ stats ✨ or something, this will help you to find those users.

It's not complete, I have compres going on, I might expand on it later.

## How to use

- Make a file called **`ids.json`**, with the following content. Get the IDs from the `Web Developer Tools` section (`CTR + SHIFT + I`):
	```yaml
	{
	    "user_id": "",
	    "session_id": ""
	}
	```
- Install **`python-requests`**
- Run **`a.py`**
