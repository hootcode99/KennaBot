# KennaBot

## What is this?
This was a Twitter bot I created at the request of one of my friends, Mckenna, that automatically replies to each of their significant other's new tweets with a sweet message, like, and repost.
This is not a malicious or spam project. Both my friend and her significant other gave permission.

I accepted the task because:
1. they were my friend
2. I wanted to learn more about building bots for Twitter (I had built bots for discord and facebook before)
3. one can never get enough practice programming 

## What is it built on?
### Tweepy 

https://www.tweepy.org/ \
https://docs.tweepy.org/

Tweepy is the best Python Twitter API handler (from my research). So I learned how to use it to leverage it for the bot.

### Repl.it
Initially, I hosted this bot on https://replit.com/ wrapped in a Flask app since Repl.it will allow you to host simple websites for free. 
Later, I ended up building a home server and moved the deployment there.


## How does it work?

The bot begins by consuming your supplied Twitter API keys and tokens. You can get your own tokens by making an account at: 
https://developer.twitter.com/
It would be best practice to store these keys/tokens as environment variables. However, for simplicity I stored them as text variables.

After consuming the the tokens and authenticating, the bot queries the Twitter API for the supplied userID to attach to the target user. It then creates a textfile (if it does not already exist) 
to log the last tweet ID that it has seen from that user. This is so that if the bot is stopped, when restarted, it can read from that file to have a record of the last tweet it saw. 
If it was simply stored in the running memory, the bot could miss tweets on restart. Note: This file is only read on restart, but is overwritten after detecting a new tweet. 

The bot then queries the API for the target user's newest tweet ID against the tweet ID stored in the file, and, if they are different, 
will reply with the desired message. It queries the API every 300 seconds to check for a new tweet and then waits to check again. When the bot responds, it also likes and retweets.
There is some terminal logging so one can see that the bot is running and monitor it's progress.


## Note
When I built this bot, the most basic access to the Twitter API was free. Unfortunately, as businesses have become aware that their data is being used to train AI models, 
it is becomming more common for them to charge for even the lowest tier. Twitter has since implemented such changes and is no longer free.
