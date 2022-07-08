import tweepy
import time
from os.path import exists
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
    user = bot_client.get_user(username="")  # Query API for target using username
    target = user.data.id  # Get TwitterID for target user
    print(f'Tracking User "@{user.data.username}"')
    print(f'TwitterID: {target}')
    previous_tweet_id = "000000000"  # Default value for first run

    if exists('last_tweet_id.txt'):  # check if the file has been created
        with open('last_tweet_id.txt', 'r') as latest_tweet_record:  # open the file that stores the last tweetID
            previous_tweet_id = latest_tweet_record.readline()  # store the tweetID from the file
            print(f'Last Replied TweetID: {previous_tweet_id}')
    else:
        last_tweet_record = open('last_tweet_id.txt', "w+")  # create the file
        last_tweet_record.write("0000000000")  # write a placeholder to the file

    # initial check to see if last found tweet from the file is still the last tweet
    latest_tweet = bot_client.get_users_tweets(id=target, exclude=["replies", "retweets"])[0][0]
    latest_tweet_id = str(latest_tweet.id)  # Get the id of the tweet as a string
    if latest_tweet_id == previous_tweet_id:
        print("----------------------")
        print("No New Tweets Found")

    while True:  # Loop the program until you stop it manually
        previous_tweet_id = get_latest_tweet(previous_tweet_id, bot_client, target)
        dots = ""
        for i in range(300, -1, -1):  # Wait timer that updates live
            if len(dots) < 3:
                dots += "."
            else:
                dots = "."
            print(f"\rChecking again in {i} seconds{dots}", end='')
            time.sleep(1)


def get_latest_tweet(previous_tweet_id, bot, user_id):
    # Query API for latest tweet from specified user (excluding replies and retweets)
    latest_tweet = bot.get_users_tweets(id=user_id, exclude=["replies", "retweets"])[0][0]

    latest_tweet_id = str(latest_tweet.id)  # Get the id of the tweet as a string
    latest_tweet_text = latest_tweet.text  # Get the text of the tweet

    if latest_tweet.created_at is None:  # Checking for tweet date-timestamp (not working)
        latest_tweet_timestamp = "{Date Not Found}"
    else:
        latest_tweet_timestamp = latest_tweet.created_at

    if latest_tweet_id != previous_tweet_id:  # If the latest tweet is new
        print("\r", end='')
        print("\n\n----------------------")
        print("NEW TWEET FOUND")
        print("----------------------")
        print(f'Tweet ID: {latest_tweet_id} - Posted {latest_tweet_timestamp}')
        print(f'Tweet Text: \n{latest_tweet_text}')

        respond(latest_tweet_id, bot)  # Call the function to respond to tweet

        return latest_tweet_id
    else:
        return previous_tweet_id


def respond(latest_tweet_id, bot):
    bot.like(latest_tweet_id)  # like the tweet
    response = bot.create_tweet(text="Default Message",
                                in_reply_to_tweet_id=latest_tweet_id)  # send response
    print("----------------------")
    response_time_stamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")  # get timestamp for response
    if response:  # confirm response
        print(f'Responded Successfully - {response_time_stamp}')
        print("----------------------")

        with open('last_tweet_id.txt', "w+") as latest_tweet_record:  # open the file
            latest_tweet_record.write(latest_tweet_id)  # write the tweetID to the file
    else:
        print('Response Failed')
        print("----------------------")


if __name__ == "__main__":
    main()
