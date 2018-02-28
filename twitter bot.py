import tweepy
from time import sleep
  
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
 
class StdOutListener(tweepy.StreamListener):
    
    def on_status(self, status):
        print('Tweet text: ' + status.text)
        api = tweepy.API(auth)
        api.update_status(status.text)
        #time.sleep(5)

        
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
    track_tag = ['#IndiaOnFastTrack']
    stream.filter(track = track_tag)
    #stream.filter(follow = ['967302676483657728']