import tweepy
import time
from datetime import datetime

# Store Key, Tokens, and Secrets
API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
BEARER_TOKEN = "" \
               ""


def main():
    bot_client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)  # Initiate Client
    print("-----BOT ACTIVATED-----")
    user = bot_client.get_user(username="clampls")  # Query API for target using username
    target = user.data.id  # Get TwitterID for target user
    print(f'Tracking user "@{user.data.username}" - ID: {target}')

    previous_tweet_id = "0"  # Default value for first run (can use file to store state later)
    while True:  # Loop the program forever
        previous_tweet_id = get_latest_tweet(previous_tweet_id, bot_client, target)
        time.sleep(1200)  # How long to wait (in seconds) before checking again


def get_latest_tweet(previous_tweet_id, bot, user_id):
    latest_tweet = bot.get_users_tweets(id=user_id)[0][0]  # Query API for latest tweet from specified user
    latest_tweet_id = latest_tweet.id  # Get the id of the tweet
    latest_tweet_text = latest_tweet.text  # Get the text of the tweet

    if latest_tweet.created_at is None:  # Check for Timestamp
        latest_tweet_timestamp = "{Date Not Found}"
    else:
        latest_tweet_timestamp = latest_tweet.created_at

    if latest_tweet_id != previous_tweet_id:  # If the latest tweet is new
        print("\nNEW TWEET")
        print("------------")
        print(f'Tweet ID: {latest_tweet_id} - Posted {latest_tweet_timestamp}')
        print(f'Tweet Text: \n{latest_tweet_text}')

        respond(latest_tweet_id, bot)  # Call the function to respond to tweet

        return latest_tweet_id
    else:
        return previous_tweet_id


def respond(latest_tweet_id, bot):
    bot.like(latest_tweet_id)  # like the tweet
    response = bot.create_tweet(text="I'm testing the bot code. If you see this, it works.",
                                in_reply_to_tweet_id=latest_tweet_id)  # send response
    print("----------------------")
    response_time_stamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")  # get timestamp for response
    if response:  # confirm response
        print(f'Responded Successfully - {response_time_stamp}')
    else:
        print('Response Failed')


if __name__ == "__main__":
    main()
