import tweepy
import json
import re
import requests              #this library for dealing with 401 protected tweets
from requests.auth import HTTPBasicAuth			#this library for dealing with 401 protected tweets

consumer_key = "40o1vq09rAl5waxx7W23W9MSR"
consumer_secret = "EoGTClhokJVVDI1N4dNlKSKuJfRckr2mlo2h4cQiAkK6boB2zK"
access_token = "834870669900935168-2I2yo4sWJIKTARj1i6M54URTYh4yn9A"
access_token_secret = "R2NsvcPMKO2Z5Ht8MpFU2G12QWNVZ18JmVdQwpohschRf"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#typeA bot this bot's duty is discover posible threats and put them in text file or db for passing data to typeB bot that is just following and preparing report for individual.

#First of all we need a start point.This can be either your account that you got keys or a starting point such as "isis twitter account"

#with this way you can expand your network.I will make it dynamic so program takes a string for starting point.


start_account_name = raw_input('Enter the starting point')       #with this method we got the starting point as string

#getting start_account's data 


start_account_detail = api.get_user(start_account_name)          #this gets the data 
start_account_followers = tweepy.Cursor(api.followers, start_account_name).items(100)  	#this gets followers for the user
print('Screen_name'+ ' ' + 'id')
print(start_account_detail.screen_name,start_account_detail.id)  




print(start_account_detail.screen_name)
print('has')
print(start_account_detail.followers_count )
print('followers')
print(start_account_name + "'s followers are:" )



response = requests.get('https://twitter.com/' + start_account_name + '/followers')   	#if you get 401 error which means tweets are protected but everytime i did this i get 200 needs to fix.


if response.status_code == 401:    
    print('Users tweets are protected')
	
elif response.status_code == 200: 			#if it wont work go back to else			
	for followers in start_account_followers:                    
		print followers.screen_name

		
		

   #break time 12.05.2017 16.22
   #todo list : fix tweets protected or not then put datas on text file.after figure out something for discover algh
   
   
   
   
   
   
   
   
   

