from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

TWITTER_ACCESS_TOKEN = "2740626538-n43SAeA78iKiXvyD2m6QsfOEQj7WU6aAYRbizPU"
TWITTER_ACCESS_TOKEN_SECRET = "eyn6eTPBdtLdEKkcdN1RXvRP6RAHo5pnmmUps7cWGbVto"

TWITTER_CONSUMER_KEY = "vUQXFJXui9O90OldhnHHloLSH"
TWITTER_CONSUMER_SECRET = "CvyO0PEOmsupoSV1FoTXiGh3DkJ8LOnrUdk2nsm9fqhmtbomVz"


class TweetFeed:
    def __init__(self):
        pass

    def run(self):
        listener = Listener()
        auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        stream.filter(track=['python', 'javascript', 'ruby'])


class Listener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == "__main__":
    TweetFeed().run()
