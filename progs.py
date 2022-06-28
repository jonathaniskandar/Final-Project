import Process
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def getCSV(df):
    df.to_csv("result/Result.csv")
    print("CSV Generated")


def getChart(positif, negatif):
    d = np.array([positif, negatif])
    pie, ax = plt.subplots()
    ax = plt.pie(d, labels=["Positif", "Negatif"], explode=[0.1, 0.1])
    # plt.savefig("result/Result.png")
    print("Chart Generated")
    return pie, ax
    # plt.show()


def sena(a):
    # a = 4 #nomor dict provider
    tweet_df, positif, negatif = Process.proses(a)
    getCSV(tweet_df)
    getChart(positif, negatif)
    # ------------------------------
    print("=====HASIL=====")
    print("hasil positif: ", positif)
    print("hasil negatif: ", negatif)
    print("total: ", positif + negatif)

    dtl = st.button('Get Details')
    if dtl:
        st.dataframe(tweet_df)
