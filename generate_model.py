# generate_model.py
from sklearn.naive_bayes import MultinomialNB
import pickle

X = [
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0]
]
y = ["Flu", "Flu", "Dengue"]

model = MultinomialNB()
model.fit(X, y)

with open('model/disease_model.pkl', 'wb') as f:
    pickle.dump(model, f)
