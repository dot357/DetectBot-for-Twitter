# DetectBot-for-Twitter
Project start 11.05.2017

Using certain algorytms detecting certain people (Such as isis sympathizers,racist cult etc) inside the twitter.

Twitter is crowded.This helps you to find wich group you want.

Detect terrorist sympathizers and report for goverment.

This can prevent terror attacks.

Stay with me.


Update 12.05.2017

I have decided to make 2 bots becouse of twitters rate limit.

bots are called typeA and typeB

TypeA bot does:

#typeA bot this bot's duty is discover posible threats and put them in text file or db for passing data to typeB bot that is just following and preparing report for individual.

#First of all we need a start point.This can be either your account that you got keys or a starting point such as "isis twitter account"

#with this way you can expand your network.I will make it dynamic so program takes a string for starting point.

TypeB bot does:


#Follow them 

#Further echantments will be added not decided the algorytm yet posible ai or machine learnign will stick with this becouse of i need to identify eighter person related the topic or not.if person related how is related and what is persons' role on that topic.This will be the hard part i think.


#update bot count 

I have decided adding two more bot called discoveryA
discoveryA is the main logic find the relations between people and the topic.
and pass them to typeB so typeB can follow them and create another list.

Changelog - 12.05.2017 Istanbul 20.31

12.05.2017 Istanbul 20.31
Now i can check the account is protected or not if protected it doesnt even bother itself to check followers list.


Changelog -12.05.2017 Istanbul 00.31

typeA is almost finnished

TypeA works like this you enter an origin point and bot checks profiles generalinfo - followers - friends and put them in to folder.
Next step will be crawling profiles from followers and following.


<b>Folder logic</b>
Origins -> screen_name(username) ->current_date -> files(generalinfo.txt-followers.txt-following.txt)
<b>General Info Logic</b>
it gets 11 variables here is the list:
ID<br />
screen_name<br />
protected(is account public or protected)<br />
description<br />
language(lang)<br />
time_zone<br />
statuses_count(how many tweet that person sent)<br />
friends_count
followers_count
favourites_count
profile_img_url

