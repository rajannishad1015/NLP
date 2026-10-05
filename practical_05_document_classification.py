from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

documents = [
    "exam timetable is announced",
    "project submission deadline",
    "college annual function",
    "sports day celebration",
    "results will be declared soon",
    "cultural fest invitation"
]
labels = [0, 0, 1, 1, 0, 1]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

model = LogisticRegression()
model.fit(X, labels)

test_doc = ["college fest celebration"]
test_vec = vectorizer.transform(test_doc)
prediction = model.predict(test_vec)
if prediction[0] == 1:
    print(test_doc, "- Prediction: Event")
else:
    print(test_doc, "- Prediction: Academic")
