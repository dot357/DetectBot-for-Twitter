import tweepy
import json
import re


consumer_key = "40o1vq09rAl5waxx7W23W9MSR"
consumer_secret = "EoGTClhokJVVDI1N4dNlKSKuJfRckr2mlo2h4cQiAkK6boB2zK"
access_token = "834870669900935168-2I2yo4sWJIKTARj1i6M54URTYh4yn9A"
access_token_secret = "R2NsvcPMKO2Z5Ht8MpFU2G12QWNVZ18JmVdQwpohschRf"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text

main_user = 'revzyn'
user = api.get_user(main_user)
isim= "JJaspoly"
print "kullanici ismi"
print user.screen_name
print "takipci sayisi"
print user.followers_count
print "takip ettikleri"

for friend in user.friends():
   print friend.screen_name
   

isim  = "JJaspoly"
   
print "takipciler"

followers = tweepy.Cursor(api.followers).items(100)

for followers in followers:                    
	print followers.screen_name
	if followers.screen_name == isim:
		followers.follow()
		print "I have just followed" + "  " + followers.screen_name


someone = api.get_user(isim)

print "Baskasinin hesabini kontrol etme kismi"
print "Temel Bilgiler"
print someone.screen_name,someone.id
print isim + "kisinin takipcileri"


print "Baskasinin hesabinin takipcilerini kontrol etme kismi"
someone_followers = tweepy.Cursor(api.followers, isim).items(100)
print "Icinde x olan kisileri takip etme kismi"
for followers in someone_followers:                    
	print followers.screen_name
	if re.search("x" , followers.screen_name):
		followers.follow()
		print "I have just followed" + " " + followers.screen_name 
	
	

	
	
