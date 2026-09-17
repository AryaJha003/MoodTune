import pandas as pd
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

import joblib


# --------------------------------------------------
# 1. Project paths
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
MODEL_DIR = PROJECT_DIR / "models"

MODEL_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# 2. Load datasets
# --------------------------------------------------

train_df = pd.read_csv(DATA_DIR / "emotion_train.csv")
test_df = pd.read_csv(DATA_DIR / "emotion_test.csv")


# --------------------------------------------------
# 3. Emotion labels
# --------------------------------------------------

emotion_names = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}


# --------------------------------------------------
# 4. Separate input and output
# --------------------------------------------------

X_train = train_df["text"].astype(str)
y_train = train_df["label"]

X_test = test_df["text"].astype(str)
y_test = test_df["label"]


# --------------------------------------------------
# 5. Create ML pipeline
# --------------------------------------------------

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
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        )
    )
])


# --------------------------------------------------
# 6. Train model
# --------------------------------------------------

print("=" * 60)
print("MOODTUNE - TRAINING EMOTION CLASSIFIER")
print("=" * 60)

print("\nTraining model...")

model.fit(X_train, y_train)

print("Training completed!")


# --------------------------------------------------
# 7. Evaluate model
# --------------------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:")
print(f"{accuracy:.4f}")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=[
            emotion_names[i] for i in sorted(emotion_names)
        ]
    )
)


# --------------------------------------------------
# 8. Save trained model
# --------------------------------------------------

model_path = MODEL_DIR / "emotion_classifier.pkl"

joblib.dump(model, model_path)

print("\nModel saved to:")
print(model_path)

print("\nTraining process completed successfully!")