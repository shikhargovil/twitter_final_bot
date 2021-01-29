import tweepy
import time

auth = tweepy.OAuthHandler('qW4jBmizR8wneXSKWXUCp1UFx', 'DJGJHWouxvCiLsUEovRqlkr0c63l181sSQpHOuxPdADWVjHPuD')
auth.set_access_token('1297164703110582274-kdNQfDNzdE5qhNSHIXpvtMIxQUJrbN', 'n6GrKZbeSO95QUfi0j1DUCDX2RPJJqDF7rR1jr9zoZ1vX')

api = tweepy.API(auth)
while True:
  user = api.get_user('Ameen91741779')
  f = user.followers_count
  api.update_profile(name=f'AMEER {f} Followers')
  print(f'AMEER {f} Followers')
  time.sleep(60)
