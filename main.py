from tweepy import Client, Paginator
from os import getenv
from dotenv import load_dotenv

load_dotenv()

api_key = getenv('API_KEY')
api_secret = getenv('API_SECRET')
access_token = getenv('ACCESS_TOKEN')
access_token_secret = getenv('ACCESS_TOKEN_SECRET')

tweet_id = getenv('TWEET_ID')

if None in [api_key, api_secret, access_token, access_token_secret, tweet_id]:
    raise Exception('You have to provide all of the following env vars: API_KEY, API_SECRET, ACCESS_TOKEN, '
                    'ACCESS_TOKEN_SECRET, and TWEET_ID.')

client = Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True
)

i = 0
for response in Paginator(client.get_liking_users, tweet_id, user_auth=True):
    users = response.data
    for user in users:
        client.block(user.id)
        i += 1
        if i % 10 == 0:
            print(f'blocked {i} accounts...')

print(f'Done.\nSuccessfully blocked {i} accounts.')
