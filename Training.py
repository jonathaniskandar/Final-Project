import joblib
from Preprocessing import *
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

dataTr = pd.read_csv('source/cs.csv', encoding='unicode_escape')
dataTr = dataTr.drop('Id', axis=1)
dataTr.rename(columns={'Text Tweet': 'Raw'}, inplace=True)

x = []
print("Proses Teks:")
for teks in dataTr.Raw:
    x.append(proses_teks(teks))
    print(len(x), "/", len(dataTr))

clean_Tweet = pd.DataFrame({'Text': x})
dataTr = pd.concat([dataTr, clean_Tweet], axis=1)
print(dataTr)

dataTr.dropna(subset=["Text"], inplace=True)
datad = ['Raw']
data = dataTr.drop(columns=datad)
# done

x_train, x_test, y_train, y_test = train_test_split(data.Text, data.Sentiment, test_size=.2)

tf = TfidfVectorizer()
xg = XGBClassifier()

model = Pipeline([('vectorizer', tf)
                     , ('classifier', xg)])

model.fit(x_train, y_train)
hasil = model.predict(x_test)

report = classification_report(y_test, hasil, output_dict=True)
print(report)

filename = 'source/XGB.sav'
joblib.dump(model, filename)
