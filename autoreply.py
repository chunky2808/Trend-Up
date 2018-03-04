import tweepy
  
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#api.update_status('Testing Reply ',970210194948009984') 

for page in tweepy.Cursor(api.user_timeline, id="").pages():
    for item in page:
        try:
                   if not item.retweeted:
                           item.retweet()
                           m = "testing"
                           t = api.update_status(status=m, in_reply_to_status_id=item.id)
                           print("printing reply...")
                           #sleep(1)
        except tweepy.TweepError as e:
                   print(e.reason)
                   #sleep(1)
                   break

        except StopIteration:
                   break
        # m = "hi"
        # t = api.update_status(status=m, in_reply_to_status_id=item.id)
        # print((item.text).encode('utf-8'))
    
