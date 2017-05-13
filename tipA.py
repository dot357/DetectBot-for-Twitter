import tweepy
import json
import re
import os 
import errno
import time
import codecs
from django.utils.encoding import smart_str       #smart_str() unicode error fix

consumer_key = "40o1vq09rAl5waxx7W23W9MSR"
consumer_secret = "EoGTClhokJVVDI1N4dNlKSKuJfRckr2mlo2h4cQiAkK6boB2zK"
access_token = "834870669900935168-2I2yo4sWJIKTARj1i6M54URTYh4yn9A"
access_token_secret = "R2NsvcPMKO2Z5Ht8MpFU2G12QWNVZ18JmVdQwpohschRf"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
current_date = time.strftime("%d-%m-%Y")

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
			
def txt(path): 															        #creates txt file at certain path
    try:
        path = open(path,'r')
    except:
		# if file does not exist, create it
		path = open(path,'w')
            



all_origins = "/root/origins/" + current_date  
mkdir_p(all_origins)



mkdir_p(path)

start_account_name = raw_input('Enter the starting point')       #with this method we got the starting point as string

fn= all_origins + "/" + "origins.txt"
txt(fn)																#creates all origins txt for getting all orrigins daily origin list
with open(fn, "a") as text_file:
	text_file.write(start_account_name + ",")


path = "/root/origins/" + start_account_name + "/" + current_date                                                  #setting up the path for starting point
mkdir_p(path)	                                                                               #calling the function for new path which is the users dir

#getting start_account's data 


start_account_detail = api.get_user(start_account_name)          #this gets the data 
start_account_followers = tweepy.Cursor(api.followers, start_account_name).items(100)  	#this gets followers for the user
start_account_friends = tweepy.Cursor(api.friends, start_account_name).items(100)		#i kept this 100 becouse of rate limits this can be dynamic for now it will stay as 100 for demo purposes
		
print('Screen_name'+ ' ' + 'id')
print(start_account_detail.screen_name,start_account_detail.id)  



#FOLLOWERS LIST START
print(" Process started" )
#break time 12.05.2017 16.22
   #todo list : fix tweets protected or not then put datas on text file.after figure out something for discover algh
   

print("Data is proccessing ... ")


			
if start_account_detail.protected != True:	    	#FIXED TWEET PROTECT 12.05.2017-20.31||finding protected account is quite tricky tried 3-4 methods nothing worked so i downloaded user data and found Protected = True so i go to that now if account is protected it shows.
	followers_path = path + "/" + "followers.txt"				#this is the followers path
	txt(followers_path)
	file = open(followers_path ,"w")
	for followers in start_account_followers:                    
		file.write(followers.screen_name + ",")					#i tried making a dir for every follower but it needs space and cpu to run so i will go with txt for every friend and follower also likes 
	file.close()	
		
else:
	print(start_account_name + 'is protected')   

print(current_date + " Daily followers added to the followers.txt" ) 
#FOLLOWERS LIST END

#FRIENDS LIST START
print("Data is proccessing ... ")

if start_account_detail.protected != True:	  
	fn = path + "/" + "friends.txt"
	txt(fn)
	file = open(fn ,"w")
	for friends in start_account_friends:                    
		file.write(friends.screen_name + ",")					
	file.close()	
		
else:
	print(start_account_name + 'is protected')   

print(current_date + " Daily friends added to the friends.txt" )
#FRIENDS LIST STOP


#details we need on general information list

fn = path + "/" + "generalinfo.txt"
txt(fn)
file = open(fn ,"w")

print("Data is proccessing ... ")
file.write(str(start_account_detail.id) + ",")
file.write(start_account_detail.screen_name + ",")
file.write(str(start_account_detail.protected) + ",")
file.write(smart_str(start_account_detail.description) + ",")
file.write(str(start_account_detail.lang) + ",")
file.write(str(start_account_detail.time_zone) + ",")
file.write(str(start_account_detail.statuses_count) + ",")
file.write(str(start_account_detail.friends_count) + ",")
file.write(str(start_account_detail.followers_count) + ",")
file.write(str(start_account_detail.favourites_count) + ",")
file.write(start_account_detail.profile_image_url + ",")

print('Data is processed in to generalinfo.txt')
file.close()  

   
   

  
   
   
#DISCOVERY BOT START


dpath = "/root/lists/" + current_date 		#level list path
mkdir_p(dpath)								
l1 = dpath + "/l1.txt"						#l1 list path
l2 = dpath + "/l2.txt"
l3 = dpath + "/l3.txt"

txt(l1)
txt(l2)
txt(l3)

def coppy_file(output,coppying):
	f = open(coppying)
	f1 = open(output, 'a')
	for line in f.readlines():
		f1.write(line)
	f1.close()
	f.close()

	
coppy_file(l1,followers_path)



   
   
   
   

