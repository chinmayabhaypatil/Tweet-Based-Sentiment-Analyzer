import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
import emoji
import preprocessor as p
#from googletrans import Translator
from mtranslate import translate
import train as t
#from py_translator import Translator

ckey="gz4VcAW0OaWuheYB3Y6LzLXOc"
csecret="PhzqOWSyZKb38iUmxjDPVZnujqt7YIwVYLRPWnNkjhzlD0TywO"
atoken="1007199770547445762-9NbAVQz4FGGwVfXgs3hig3TfAk6bfM"
asecret="nyqZ9jwBmAnexMEyVyThP14ILIY97cWL8P0u0kir9bCAn"

#translator=Translator()
class listener(StreamListener):

    '''def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["full_text"]
        print(ascii(tweet),"\n\n\n")'''

    def on_status(self, status):
        
        #try:
            
        if hasattr(status, 'retweeted_status') and hasattr(status.retweeted_status, 'extended_tweet'):
            #print(status.retweeted_status.extended_tweet['full_text'])
            tweet=status.retweeted_status.extended_tweet['full_text']
                    
        if hasattr(status, 'extended_tweet'):
            #print(status.extended_tweet['full_text'])
            tweet=status.extended_tweet['full_text']
                    
        else:
            #print(status.text)
            tweet=status.text

        tweet=emoji.demojize(tweet)
        tweet=p.clean(tweet)
        tweet=translate(tweet,"en","auto")
        #tweet=translator.translate(tweet) googletrans
        #tweet=Translator().translate(text=tweet,dest="en").text py_translator
        #tweet=tweet.text googletrans

        sentiment_value,confidence=t.sentiment(tweet)
        print(sentiment_value,"\n\n\n")
        f=open("twitter-out.txt",'a')
        f.write(sentiment_value+"\n")
            
                
        #except:
            #print('attribute error: ' + ascii(status.text),"\n\n\n")
            #pass

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener(),tweet_mode='extended')
twitterStream.filter(track=["modi"])




'''import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from googletrans import Translator
import re
import json
import preprocessor as p
import train as t
import emoji

ckey="gz4VcAW0OaWuheYB3Y6LzLXOc"
csecret="PhzqOWSyZKb38iUmxjDPVZnujqt7YIwVYLRPWnNkjhzlD0TywO"
atoken="1007199770547445762-9NbAVQz4FGGwVfXgs3hig3TfAk6bfM"
asecret="nyqZ9jwBmAnexMEyVyThP14ILIY97cWL8P0u0kir9bCAn"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
translator=Translator()

search_tweets = api.search('obama',count=20,tweet_mode='extended')
for tweet in search_tweets:
    
    if 'retweeted_status' in tweet._json:
        tweet=(tweet._json['retweeted_status']['full_text'])
        #tweet=translator.translate(tweet)
        #tweet=tweet.text
        #tweet=p.clean(tweet)
        tweet=emoji.demojize(tweet)
        tweet=p.clean(tweet)
        tweet=translator.translate(tweet)
        tweet=tweet.text
        #tweet = re.sub(r"http\S+", "", tweet)
        if(tweet==''):
            pass
        else:
            sentiment_value,confidence=t.sentiment(tweet)
            print(tweet,sentiment_value,confidence,"\n\n\n")

    else:
        tweet=(tweet.full_text)
        #tweet=translator.translate(tweet)
        #tweet=tweet.text
        #tweet=p.clean(tweet)
        tweet=emoji.demojize(tweet)
        tweet=p.clean(tweet)
        tweet=translator.translate(tweet)
        tweet=tweet.text
        #tweet = re.sub(r"http\S+", "", tweet)
        sentiment_value,confidence=t.sentiment(tweet)
        print(tweet,sentiment_value,confidence,"\n\n\n")'''
