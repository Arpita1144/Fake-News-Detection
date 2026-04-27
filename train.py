import pandas as pd
import pickle
import re
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

# Load dataset
fake_df = pd.read_csv("../data/Fake.csv")
true_df = pd.read_csv("../data/True.csv")

# label encoding
fake_df["label"] = 0
true_df["label"] = 1

# combine datasets
df = pd.concat([fake_df[["text", "label"]], true_df[["text", "label"]]], ignore_index=True)
 
#  shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print("Columns in dataset:", df.columns)

# If only text exists, use it directly
if "title" in df.columns:
    df["text"] = df["title"].fillna("") + " " + df["text"].fillna("")


# text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

df["text"] = df["text"].apply(clean_text)

X = df["text"]
y = df["label"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
      df["text"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

# Vectorization
vectorizer = TfidfVectorizer( max_features=40000,
    ngram_range=(1,2),
    stop_words="english",
    lowercase=True,
    strip_accents="unicode")

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# Train model
param_grid = {
    "C": [0.1, 1, 2, 5],
    "solver": ["liblinear"]
}

grid = GridSearchCV(
    LogisticRegression(class_weight="balanced", max_iter=2000),
    param_grid,
    cv=3,
    scoring="f1_weighted",
    n_jobs=-1   # uses all CPU cores
)

grid.fit(X_train_vectorized, y_train)

model = grid.best_estimator_

# Evaluate
y_pred = model.predict(X_test_vectorized)
print(classification_report(y_test, y_pred))

preds = model.predict(X_test_vectorized)
print("Accuracy:", accuracy_score(y_test, preds))

# ✅ SAVE MODEL & VECTORIZER (ADD HERE AT THE END)
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model and vectorizer saved successfully!")
