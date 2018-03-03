import tweepy
import sys
from time import sleep

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
 
class StdOutListener(tweepy.StreamListener):
    
    def on_status(self, status):
        print(('Tweet text: ' + status.text).encode('utf-8'))
        api = tweepy.API(auth)
        try:
            if status.text != '\n':
                api.update_status(status.text)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
        sleep(5)     
        
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True 

    def on_timeout(self):
        print('Timeout...')
        return True

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    listener = StdOutListener()
    stream = tweepy.Stream(auth, listener)
    #follow_id =  ['967302676483657728']
    track_tag = ['#TripuraElection2018']
    stream.filter(track = track_tag)
    #stream.filter(follow = ['967302676483657728']