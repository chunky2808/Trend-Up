import tweepy
from time import sleep
  
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("Chose option 1) For Just Copying Tweet and automating printing it from your account.")
print("Chose option 2) For Retweeting,following,mark tweet as favourite")

a = input()


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



if a==1 :
  listener = StdOutListener()
  stream = tweepy.Stream(auth, listener)
  #follow_id =  ['967302676483657728']
  track_tag = ['#TripuraElection2018']
  stream.filter(track = track_tag)
  #stream.filter(follow = ['967302676483657728']   

else:
  for tweet in tweepy.Cursor(api.search, q='#WhySalaryStopped',since='2018-03-02',until='2018-03-04').items():
      try:
         tweet.retweet()
         tweet.favorite()
         tweet.user.follow()
         
      except tweepy.TweepError as e:
          print(e.reason)

      except StopIteration:
          break
