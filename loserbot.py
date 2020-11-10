#!/usr/bin/python

import datetime, time
import pickle
import signal, sys
from TweepyHelper import TweepyHelper


def process_tweet_for_user(username, last_id, reply_message):
	print("checking for tweets for %s" % username)
	helper = TweepyHelper()
	user = helper.get_user(username)
	tweet = helper.get_last_tweet(user.id)
	if tweet:
		if tweet.id != last_id:
			print("new tweet [%s] found at %s " % (tweet.id, tweet.created_at))
			print(helper.get_tweet_text(tweet.id))				
			message = "@%s %s" % (username, reply_message)
			helper.tweet_reply(tweet.id, message)
			last_id = tweet.id
	return last_id

def main():
	print("--- LoserBot 1.0 ---")
	donald_tweet_id = 0
	junior_tweet_id = 0
	eric_tweet_id = 0
	ivanka_tweet_id = 0
	try:
		while True:
			donald_tweet_id = process_tweet_for_user('realDonaldTrump', donald_tweet_id, "#LOSER")
			junior_tweet_id = process_tweet_for_user('DonaldJTrumpJr', junior_tweet_id, "#LOSER")
			eric_tweet_id = process_tweet_for_user('EricTrump', eric_tweet_id, "#LOSER")
			ivanka_tweet_id = process_tweet_for_user('IvankaTrump', ivanka_tweet_id, "#LOSER")
			time.sleep(100)
	except KeyboardInterrupt:
		print("Quitting...")
		sys.exit()

def test():
	print("getting user")
	helper = TweepyHelper()
	donald_user = helper.get_user('realDonaldTrump')  # id = 25073877
	print("looking for tweets")
	tweet = helper.get_last_tweet(donald_user.id)
	print(tweet)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
  #test()
