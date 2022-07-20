import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import sqlite3

con = sqlite3.connect(r"C:\Users\ssvis\Recommendation\db.sqlite3")
df = pd.read_sql_query("Select * from recommender_system_book", con)

def combine_features(data):
    features = []
    for i in range(0, len(df)):
        features.append(str(data["title"][i])+""+str(data["author"][i])+""+str(data["year"][i]))
    return features
    
def recommendation_system(book_id):
    df["combined_features"] = combine_features(df)
    cm = CountVectorizer().fit_transform(df["combined_features"])
    cs = cosine_similarity(cm)

    title = df["title"][0]
    scores = list(enumerate(cs[book_id]))

    sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True)
    sorted_scores = sorted_scores[1:]
    j = 0
    book_titles = []
    for item in sorted_scores:
        book_title = df[df.book_id == item[0]]["title"].values[0]
        book_titles.append(book_title)
        j = j+1
        if j >=5:
            break
        return book_titles
con.close()