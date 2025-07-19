# Define the search query
search_query = "#AI -filter:retweets"  # Example query

# Search for tweets
tweets = tweepy.Cursor(api.search,
                      q=search_query,
                      lang="en",
                      result_type="recent").items(1000)

# Collect tweet text
tweet_text = []
for tweet in tweets:
    tweet_text.append(tweet.text)