from tweepy import Client, Paginator
from os import getenv
from dotenv import load_dotenv
import argparse

load_dotenv()

api_key = getenv('API_KEY')
api_secret = getenv('API_SECRET')
access_token = getenv('ACCESS_TOKEN')
access_token_secret = getenv('ACCESS_TOKEN_SECRET')
my_user_id = getenv('MY_USER_ID')
tweet_id = getenv('TWEET_ID')

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--skip_following", help="Skip accounts that you have followed")
parser.add_argument("-i", "--ignore", nargs='+', type=str, help="ignore and skip block this usernames")
args = parser.parse_args()

if None in [api_key, api_secret, access_token, access_token_secret, tweet_id]:
    raise Exception('You have to provide all of the following env vars: API_KEY, API_SECRET, ACCESS_TOKEN, '
                    'ACCESS_TOKEN_SECRET, MY_USER_ID, and TWEET_ID.')

client = Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True
)

followings = []
for response in Paginator(client.get_users_following, id=my_user_id, user_auth=True):
    fetched_followings = response.data
    if not fetched_followings:
        print(f'in get_users_following, response: {response}')
        continue
    for following in fetched_followings:
        followings.append(following.id)

i = 0
for response in Paginator(client.get_liking_users, tweet_id, user_auth=True):
    users = response.data
    if not users:
        print(f'in get_liking_users, response: {response}')
        continue
    for user in users:
        if (user.username in args.ignore) or (args.skip_following and user.id in followings):
            print(f'{user.username} liked but not blocked')
            continue
        client.block(user.id)
        i += 1
        if i % 10 == 0:
            print(f'blocked {i} accounts...')

print(f'Done.\nSuccessfully blocked {i} accounts.')
