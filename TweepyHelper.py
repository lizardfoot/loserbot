# -------------------------------------
# Tweepy Helper
# v.2 with Tweepy 3.9.0
# -------------------------------------
import tweepy
import json

class TweepyHelper:
  # Twitter API Info

  APP_NAME="loserbot_1"
  OWNER = "7Heads7Horns"
  OWNER_ID = "3894487535"
  CALLBACK_URL = "http://127.0.0.1"
  TOKENS_FILE = "credentials.json"
  AUTH = None
  API = None
  KEYS = {}     # dictionary to hole tokens and access keys
  CREDS = None  # JSON object to store tokens and access keys

  def __init__(self): 
    self.load_credentials()
    self.AUTH = tweepy.OAuthHandler(self.CREDS['consumer_key'], self.CREDS['consumer_secret'])
    self.AUTH.set_access_token(self.CREDS['access_token_key'], self.CREDS['access_token_secret'])
    self.API = tweepy.API(self.AUTH)

  def load_credentials(self):
    try:
      with open(self.TOKENS_FILE) as f:
        self.CREDS = json.loads(f.read())
    except:
      print "ERROR: Unable to load credentials"
      exit(1)

  # API.get_user(id/user_id/screen_name)
  def get_user(self, id): #id/user_id/screen_name
    return self.API.get_user(id)
  # API.me()
  def get_myself(self):
    return self.API.me()

  # API.update_status(status[, in_reply_to_status_id][, lat][, long][, source][, place_id])
  def tweet(self, status):
    try:
      self.API.update_status(status)
    except:
      pass
      
  # Hint: prepend @screenname to the status text
  def tweet_reply(self, tweet_id, status):
    try:
      self.API.update_status(status, in_reply_to_status_id = tweet_id)
    except:
      pass

  # API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])
  # Hint: tweets are returned in a list sorted newest to oldest
  def get_tweets(self, user_id, count = 10, page = 1, since_id = 0):
    if since_id > 0:
      return self.API.user_timeline(user_id, count=count, page=page, since_id=since_id)
    else:
      return self.API.user_timeline(user_id, count=count, page=page)

  def get_last_tweet(self, user_id, since_id = 0):
    tweet = None
    data = self.API.user_timeline(user_id, count=1) #, since_id=since_id)
    if len(data) > 0:
      tweet = data[0]
    return tweet

  def get_tweet_text(self, tweet_id):
    status = self.API.get_status(tweet_id, tweet_mode="extended")
    return status.full_text

  def test(self):
    tweet = None
    print("test: get user...")
    donald = self.get_user("realDonaldTrump")
    #donald = self.get_user("lizardfoot")
    #print(donald)
    print("test: get timeline...")
    timeline = self.API.user_timeline(donald.id)
    #print(timeline)
    print("test: get cursor...")
    #cursor = tweepy.Cursor(timeline)
    cursor = tweepy.Cursor(self.API.user_timeline, id=donald.id)
    #print(cursor)
    if cursor:
      print("test: iterate items...")
      for tweet in cursor.items(1):
        print("%s : %s" % (tweet.id, tweet.created_at))
        status = self.API.get_status(tweet.id, tweet_mode="extended")
        print(status.full_text)
    else:
      print("error: cursor is null")
    return tweet

def test():
  helper = TweepyHelper()
  helper.test()
  #user = helper.get_user('lizardfoot')
  #print "Screen Name: %s" % user.screen_name
  #print "Followers: %s" % user.followers_count
  #tweet = helper.get_tweets(user.id, count=1)
  #print tweet[0].id
  #print tweet[0].text

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  test()
