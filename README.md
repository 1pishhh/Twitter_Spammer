
# Twitter_Spammer
- Hello This is a simple script in Python 3.9.5.
- The use of this script is to send as fast of a tweet to Twitter as... 
- fast as possible and at the same time test how many tweets can be sent in a period time.


# Instructions
- Please change the api-key codes in the script ( Maybe add a feature to enter the api-keys???)

- Besides that Please don't use for a malicious intent. I am sure no one will do but still please don't. 

- Also to adjust the interval at which you tweet please change integer values in: 
```diff 
- " sleep(1 - time() % 1) "
```
- To tweet with a hashtag just add this in the api.update_status("TEXT"):
```diff 
- api.update_status("#HASHTAG "+ update_tweets)
```
