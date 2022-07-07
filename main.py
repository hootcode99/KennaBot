import tweepy
import time

# Store Key, Tokens, and Secrets
API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
BEARER_TOKEN = "" \
               ""


def main():
    bot_client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)  # Initiate Client
    previous_tweet_id = "0"
    user = "342366464"

    while True:
        previous_tweet_id = get_latest_tweet(previous_tweet_id, bot_client, user)
        time.sleep(600)


def get_latest_tweet(previous_tweet_id, bot, user_id):
    latest_tweet = bot.get_users_tweets(id=user_id)[0][0]  # Query for latest tweet from user
    latest_tweet_id = latest_tweet.id  # Get the id of the latest tweet
    latest_tweet_text = latest_tweet.text  # Get the text of the tweet

    if latest_tweet_id != previous_tweet_id:  # If the latest tweet is new
        print("NEW TWEET")
        print("------------")
        print(f'Tweet ID: {latest_tweet_id}')
        print(f'Tweet Text: \n{latest_tweet_text}')
        respond(latest_tweet_id, bot)
        return latest_tweet_id

    else:
        return previous_tweet_id


def respond(latest_tweet_id, bot):
    bot.create_tweet(text="I'm testing the bot code. If you see this, it works.", in_reply_to_tweet_id=latest_tweet_id)
    print("----------------------")
    print("Responded Successfully")


if __name__ == "__main__":
    main()
