'''
    " Grab your dick if you love big poppa " - Big Poppa
    By: Pishh(P155H)
    Date: 7/5/2021
    Ver: 0.01
    Title: Twitter Spammer





'''

import random, tweepy
from time import time, sleep

# twitter api shit
consumer_key = 'Consumer Key'
consumer_secret = 'Consumer Secret'
access_token = 'Access Token'
access_token_secret = 'Access Token Secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

   
def gen(leng):
    try:
        get_C = unichr
    except NameError:
        get_C = chr
    
    #Update to include more ranges
    uni_range = [
        ( 0x0021, 0x0021 ),( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ), 
        ]
    char_list = [
        get_C(point) for uni_rangeRn in uni_range
        for point in range(uni_rangeRn[0], uni_rangeRn[1] + 1)
        ]
    return ''.join(random.choice(char_list) for i in range(leng))

# Main

def main():
    while True:
        try:
            sleep(1 - time() % 1)    # basic timer / 
            update_tweets = (gen(10)) # The number specifys length of the tweet
            api.update_status(update_tweets)
        except KeyboardInterrupt: # ctrl + alt + c for me 
            print('The User stopped the spammer')
            break

if __name__ == "__main__":
    main()
