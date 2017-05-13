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

<strong>Changelog </strong>- <i>12.05.2017 Istanbul 20.31</i>


Now i can check the account is protected or not if protected it doesnt even bother itself to check followers list.


<strong>Changelog </strong>-<i>12.05.2017 Istanbul 00.31</i>

typeA is almost finnished

TypeA works like this you enter an origin point and bot checks profiles generalinfo - followers - friends and put them in to folder.
Next step will be crawling profiles from followers and following.


<b>Folder logic</b><br/>
Origins -> screen_name(username) ->current_date -> files(generalinfo.txt-followers.txt-following.txt)<br />
<b>General Info Logic</b><br/>
it gets 11 variables here is the list:<br/>
<ol>
<li>ID</li>
<li>screen_name</li>
<li>protected(is account public or protected)</li>
<li>description</li>
<li>language(lang)</li>
<li>time_zone</li>
<li>statuses_count(how many tweet that person sent)</li>
<li>friends_count</li>
<li>followers_count</li>
<li>favourites_count</li>
<li>profile_img_url</li>
</ol>


<strong>Changelog </strong>-<i>13.05.2017 Istanbul 16.21</i><br />

Created daily origin list which is under the origins file
origins->current_date->origins.txt
with this attribute i can track daily origin point so i dont miss anything.Also i can make it automated system becouse of i have the list of person who to look up.
