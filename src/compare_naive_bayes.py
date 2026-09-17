import pandas as pd
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

import joblib


# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
MODEL_DIR = PROJECT_DIR / "models"

MODEL_DIR.mkdir(exist_ok=True)


# Load datasets
train_df = pd.read_csv(DATA_DIR / "emotion_train.csv")
test_df = pd.read_csv(DATA_DIR / "emotion_test.csv")


# Input and output
X_train = train_df["text"].astype(str)
y_train = train_df["label"]

X_test = test_df["text"].astype(str)
y_test = test_df["label"]


# Emotion names
emotion_names = [
    "sadness",
    "joy",
    "love",
    "anger",
    "fear",
    "surprise"
]


# Create pipeline
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            max_features=20000,
            ngram_range=(1, 2),
            sublinear_tf=True
        )
    ),
    (
        "classifier",
        MultinomialNB()
    )
])


# Train
print("=" * 60)
print("MOODTUNE - MODEL 3: MULTINOMIAL NAIVE BAYES")
print("=" * 60)

print("\nTraining Multinomial Naive Bayes...")

model.fit(X_train, y_train)

print("Training completed!")


# Evaluate
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:")
print(f"{accuracy:.4f}")

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions,
        target_names=emotion_names
    )
)


# Save model
model_path = MODEL_DIR / "naive_bayes_emotion_classifier.pkl"

joblib.dump(model, model_path)

print("\nModel saved to:")
print(model_path)

print("\nModel 3 completed successfully!")