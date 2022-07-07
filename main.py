import tweepy

# Key, Tokens, and Secrets
API_KEY = "ZcyTQItoXFoiqZv3ax0oQ10fT"
API_SECRET = "Zq3j7Bw4eU3U2jqsp0EClqDeQhKo6QtXFx7VSTddL7oYV0wXQ8"
ACCESS_TOKEN = "2155959079-Khc9DWv4z4U1JcjdqzJy2qAyCxb3ERdJYEaO7Ph"
ACCESS_TOKEN_SECRET = "WlC0F8YOlsIP55JI1HEW6YcTylMueO1b2oiOTMHqKq1RF"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAPYregEAAAAAotLrlCG%2B3TIY1TcOau8" \
               "iNqObxm0%3D3Fj4g334oYZvkaL6YMPZXJofOCGsZP9qyWDGgcKqBn94jbQiuX"

# Authenticate to Twitter
# auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#
# api = tweepy.API(auth)
client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
new_tweet = client.create_tweet(text='First tweet from #python !')
