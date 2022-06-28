import joblib
from Tweets import *
from Preprocessing import *

model = joblib.load('source/XGB6.sav')


def providers(n):
    provider = {
        0: "IndiHome",
        1: "FirstMediaCares",
        2: "BiznetHome",
        3: "MyRepublicID",
        4: "MNCPlayID",
        5: "TransvisionID",
        6: "di_cbn",
        7: "megavision_id",
        8: "groovyid"
    }
    return provider.get(n, "")


def proses(n):
    proses = st.progress(0)
    banyak = 250  # banyaknya data yang diambil
    provider = providers(n)
    tweet_df = cari(provider, banyak)

    proses.progress(33)
    b = st.info(' Preprocessing Tweets... ')
    print("===== Preprocessing Tweets... =====")
    data = []
    tweetdf = tweet_df
    prepro = st.progress(0)
    for x in range(len(tweetdf)):
        data.append(proses_teks(tweetdf.tweet[x]))
        print("  ", len(data), "/", len(tweetdf))
        prepro.progress(int(x / len(tweetdf) * 100))

    for i in range(len(tweetdf)):
        while tweetdf.like[i] > 0:
            data.append(data[i])
            tweetdf.like[i] = tweetdf.like[i] - 1

    prepro.empty()
    proses.progress(66)
    b.info(' Predicting... ')
    print("===== Predicting... ======")
    hpredict = model.predict(data).tolist()
    tweet_df['result'] = hpredict[:len(tweetdf)]
    positif = hpredict.count("positive")
    negatif = hpredict.count("negative")

    proses.progress(100)
    b.success(' Done ')
    return tweet_df, positif, negatif, provider
