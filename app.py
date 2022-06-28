import streamlit as st
import progs
import Process
from datetime import datetime
import time

start = time.time()
now = datetime.now()
currenttime = now.strftime("%d/%m/%Y %H:%M:%S")


def result(a):
    st.write('----------')
    tweet_df, positif, negatif, prov = Process.proses(a)
    total = positif + negatif
    posper = round(positif / total * 100, 2)
    negper = round(negatif / total * 100, 2)
    durasi = round((time.time() - start) / 60, 3)
    print(f'time processing = {durasi} minutes')

    st.write(f"""
    ----------
    ## Sentiment Result of **@{prov}**
    **{currenttime}**
    ###
    ### Total: {total} Tweets
    Took **{durasi}** minutes
    """)
    if positif > negatif:
        st.success(f'Sentiment for @{prov} is POSITIVE')
    elif negatif > positif:
        st.error(f'Sentiment for @{prov} is NEGATIVE')
    else:
        st.warning(f'Sentiment for @{prov} is NEUTRAL')

    col1, col2 = st.columns(2)
    col1.write(f"""
    # Positive:
    ## {posper}%
    ## {positif}/{total}
    """)
    col2.write(f"""
    # Negative:
    ## {negper}%
    ## {negatif}/{total}
    """)

    st.write("""
        ----------
        ### Chart
        """)
    pie, ax = progs.getChart(positif, negatif)
    st.pyplot(pie)
    st.write("""
    ----------
    ### Result Details
    """)
    hsl = st.dataframe(tweet_df)
    st.download_button(
        'Download Data',
        tweet_df.to_csv(),
        f'{prov}_sentiment.csv',
        'text/csv'
    )


title, button = st.columns(2)
with title:
    st.write("""
    # Social Media Analysis Apps
    Select one of these ISP
    """)
with button:
    bt0 = st.button('IndiHome')
    bt1 = st.button('First Media')
    bt2 = st.button('Biznet')
    bt3 = st.button('My Republic')
    bt4 = st.button('MNC Play')
    bt5 = st.button('Transvision')
    bt6 = st.button('CBN')
    bt7 = st.button('Megavision')
    bt8 = st.button('Groovy')

if bt0:
    result(0)
if bt1:
    result(1)
if bt2:
    result(2)
if bt3:
    result(3)
if bt4:
    result(4)
if bt5:
    result(5)
if bt6:
    result(6)
if bt7:
    result(7)
if bt8:
    result(8)
