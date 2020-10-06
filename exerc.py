from TwitterSearch import *
try:

    ts = TwitterSearch(
        consumer_key = 'jFGmQqhnRbztcUi4ZUpViNKfx',
        consumer_secret = 'K3w9Dr1DufOWHMlcMmsZDqyAG6qrjZhQEz6BClqM5o4RtaKCSK',
        access_token = '1634140831-N8dFUxTX06YSjI6NbemfbZUD0zuljLD3eydmZFt',
        access_token_secret = 'g5g2sKRTnPEzHI3baK0MS7aLDkuujEPGFR9wzdH3mS54j'
     )

    tso = TwitterSearchOrder()
    tso.set_keywords(['raspagem de dados'])
    tso.set_language('pt')
    i=0
    
    arquivo = open("texto.txt", "w")
    tweets = []


    for tweet in ts.search_tweets_iterable(tso):
        i = i+1
        if i == 11:
            break
        else:
            tweets.append(' \n @%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
            
    arquivo.writelines(tweets)
    arquivo.close()

except TwitterSearchException as e:
    print(e)# -*- coding: utf-8 -*-


