import tweepy
import json
import re
import os 
import errno

consumer_key = "40o1vq09rAl5waxx7W23W9MSR"
consumer_secret = "EoGTClhokJVVDI1N4dNlKSKuJfRckr2mlo2h4cQiAkK6boB2zK"
access_token = "834870669900935168-2I2yo4sWJIKTARj1i6M54URTYh4yn9A"
access_token_secret = "R2NsvcPMKO2Z5Ht8MpFU2G12QWNVZ18JmVdQwpohschRf"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


#typeA bot this bot's duty is discover posible threats and put them in text file or db for passing data to typeB bot that is just following and preparing report for individual.

#First of all we need a start point.This can be either your account that you got keys or a starting point such as "isis twitter account"

#with this way you can expand your network.I will make it dynamic so program takes a string for starting point.

path = "/root/origins/"                                                             #first path for origins dirrectory 

def mkdir_p(path): 															        #this function checks if directory exist or not if it isnt creates dirrectory
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise







mkdir_p(path)

start_account_name = raw_input('Enter the starting point')       #with this method we got the starting point as string

path = "/root/origins/" + start_account_name                                                   #setting up the path for starting point
mkdir_p(path)	                                                                               #calling the function for new path which is the users dir

#getting start_account's data 


start_account_detail = api.get_user(start_account_name)          #this gets the data 
start_account_followers = tweepy.Cursor(api.followers, start_account_name).items(100)  	#this gets followers for the user
print('Screen_name'+ ' ' + 'id')
print(start_account_detail.screen_name,start_account_detail.id)  



#FOLLOWERS LIST START
print(start_account_detail.screen_name)
print('has')
print(start_account_detail.followers_count )
print('followers')
print(start_account_name + "'s followers are:" )



#break time 12.05.2017 16.22
   #todo list : fix tweets protected or not then put datas on text file.after figure out something for discover algh
   




			
if start_account_detail.protected != True:	    	#FIXED TWEET PROTECT 12.05.2017-20.31||finding protected account is quite tricky tried 3-4 methods nothing worked so i downloaded user data and found Protected = True so i go to that now if account is protected it shows.
	for followers in start_account_followers:                    
		print followers.screen_name					#i tried making a dir for every follower but it needs space and cpu to run so i will go with txt for every friend and follower also likes 
		
		
else:
	print(start_account_name + 'is protected')   

 
#FOLLOWERS LIST END
#details we need on general information list
print(start_account_detail.profile_image_url)
print(start_account_detail.id)
print(start_account_detail.screen_name)
print(start_account_detail.name)
print(start_account_detail.description)
print(start_account_detail.lang)
print(start_account_detail.time_zone)
print(start_account_detail.friends_count)
print(start_account_detail.followers_count)
print(start_account_detail.favourites_count)

   
   
  
   
   
   
   
   
   
   
   

