import tweepy
from time import sleep

#Oauth required for using twitter API(enter your fields in between '')
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
#Oauth required for using twitter API(enter your fields in between '')

#Oauth verification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#Oauth verification

print("Chose option 1) For Just Copying Tweet and automating printing it from your account.")
print("Chose option 2) For Just Copying Tweet from accounts which you are following and automating printing it from your account")
print("Chose option 3) For Retweeting,following,mark tweet as favourite")
print("Chose option 4) For Replying on all tweets of a particular account")

a = input()

class option1(tweepy.StreamListener):
    
    def on_status(self, status):
        print(('Tweet text: ' + status.text).encode('utf-8'))#encoding
        api = tweepy.API(auth)
        try:
            if status.text != '\n':
                api.update_status(status.text)#update data to twitter account
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


class option2(tweepy.StreamListener):
    
    def on_status(self, status):
        print(('Tweet text: ' + status.text).encode('utf-8'))#encoding
        api = tweepy.API(auth)
        try:
            if status.text != '\n':
                api.update_status(status.text)#update data to twitter account
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


#For Just Copying Tweet and automating printing it from your account.

if a==1 :
  listener = option1()
  stream = tweepy.Stream(auth, listener)
  #follow_id =  ['967302676483657728']
  track_tag = ['#TripuraElection2018']
  stream.filter(track = track_tag)
  #stream.filter(follow = ['967302676483657728']  

#For Just Copying Tweet and automating printing it from your account.

#For Just Copying Tweet from accounts which you are following and automating printing it from your account

elif a==2 :
  listener = option2()
  stream = tweepy.Stream(auth, listener)
  follow_id =  ['967302676483657728']
  #track_tag = ['#TripuraElection2018']
  #stream.filter(track = track_tag)
  stream.filter(follow = ['967302676483657728'])

#For Just Copying Tweet from accounts which you are following and automating printing it from your account"

#For Retweeting,following,mark tweet as favourite

elif a==3 :
  for tweet in tweepy.Cursor(api.search, q='#WhySalaryStopped',since='2018-03-02',until='2018-03-04').items():
      try:
         tweet.retweet()
         tweet.favorite()
         tweet.user.follow()
         sleep(3)
         
      except tweepy.TweepError as e:
          print(e.reason)

      except StopIteration:
          break

#For Retweeting,following,mark tweet as favourite

#For Replying on all tweets of a particular account

else:
  for page in tweepy.Cursor(api.user_timeline, id="967302676483657728").pages():
    for item in page:
        try:
                   if not item.retweeted:
                           item.retweet()
                           message = "testing" #your message
                           t = api.update_status(status=message, in_reply_to_status_id=item.id)
                           print("printing reply...")
                           sleep(3)
        except tweepy.TweepError as e:
                   print(e.reason)
                   sleep(3)
                   break

        except StopIteration:
                   break
        # m = "hi"
        # t = api.update_status(status=m, in_reply_to_status_id=item.id)
        # print((item.text).encode('utf-8'))

# For Replying on all tweets of a particular account
