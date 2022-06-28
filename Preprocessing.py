from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
import pandas as pd
import re

emot = pd.read_csv('source/master_emoji.csv', encoding='unicode_escape')
emot_drop = ['ID', 'Sentiment', 'Makna Emoji', 'Special Tag']
emot = emot.drop(columns=emot_drop)

tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9_]+'  # menghilangkat username jika twitter
pat2 = r'https?://[^ ]+'  # menghilangkan situs website
combined_pat = r'|'.join((pat1, pat2))  # join pat1 dan pat 2
www_pat = r'www.[^ ]+'


def proses_teks(teks):
    soup = BeautifulSoup(teks, 'lxml')
    souped = soup.get_text()
    try:
        teks = souped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        teks = souped
    teks_bersih = re.sub('<PROVIDER_NAME>', '', re.sub('<URL>', '', re.sub('<USER_MENTION>', '',
                                                                           re.sub('<PRODUCT_NAME>', '',
                                                                                  re.sub('<USERNAME>', '', teks)))))
    teks_bersih = re.sub("[^a-zA-Z0-9]", " ", (re.sub(www_pat, '', re.sub(combined_pat, '', teks_bersih)).lower()))
    teks_bersih = ' '.join([word for word in teks_bersih.split() if word not in emot])
    # teks_bersih = stemmer.stem(teks_bersih) #bikin lama
    return (" ".join([x for x in tok.tokenize(teks_bersih) if len(x) > 1])).strip()
