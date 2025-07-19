import tweepy

# Twitter API credentials
consumer_key = "your-consumer-key-here"
consumer_secret = "your-consumer-secret-here"
access_token = "your-access-token-here"
access_token_secret = "your-access-token-secret-here"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth, wait_on_rate_limit=True)