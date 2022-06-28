import tweepy as tw
import pandas as pd
import streamlit as st

api_key = 'eOhmXmKmC9064rAlVPtmQrDBV'
api_secret_key = '2LPPs2xy9arIspvc4NGdXxwmiJ4Txz3r2YA5iYeRkOI0mXQz1G'
access_token = '1447584664693051393-0BtgYfVGjcfjULQht0Pe9FjDJ4Pqc4'
access_token_secret = 'Cr4yCB2nWfKFmitRKhiaUmmbZABfzTAhFaml0R8Ydz0Sv'
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


def cari(n, x):
    a = st.spinner(' Retrieving Tweets... (Might take 1.5 Minutes) ')
    with a:
        print("===== Retrieving Tweets... =====")
        key_words = f"@{n} -has:media -has:links -is:retweet"
        search_result = tw.Cursor(api.search_tweets, q=key_words, lang="id", truncated=True).items(x)
        crawling_result = [api.get_status(data.id, tweet_mode="extended") for data in search_result]
        tweet_list = [[status.user.screen_name, status.full_text, status.favorite_count] for status in crawling_result]
        tweet_df = pd.DataFrame(data=tweet_list, columns=["username", "tweet", "like"])
    return tweet_df
