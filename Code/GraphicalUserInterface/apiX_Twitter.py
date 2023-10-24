import tweepy

class ApiX_Twitter:
    def __init__(self, publishText=None):
        self.publishTest = publishText

        self.consumer_key = 'DZ82HcqR1nSCxTNYgpQekYJ7i'
        self.consumer_secret = 'RularTLK5dSP3JDT17ZoXEueigMPGXVq2HIfFCGJDSbOt1lQbI'

        self.access_token = '1716816436126203904-zcaCY03HorGtSPni9KSr4ZUpvV5efk'
        self.access_token_secret = 'q5ff7WHTD2J23qgwEA7plA2m4c2hIXwsgjimhBJ5GfFXf'

        self.createCliente()
    
    def createCliente(self):
        self.client = tweepy.Client(consumer_key=self.consumer_key, consumer_secret=self.consumer_secret, access_token=self.access_token, access_token_secret=self.access_token_secret)
        
    def publishTweet(self, publishText):
        if publishText is not None:
            try:
                self.client.create_tweet(text=publishText)
            except:
                print("Error al publicar el tweet")
        