import pandas as pd
from pathlib import Path

# Find project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load training dataset
df = pd.read_csv(DATA_DIR / "emotion_train.csv")

# Emotion mapping
emotion_names = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

df["emotion"] = df["label"].map(emotion_names)

print("=" * 50)
print("MOODTUNE - EMOTION DATASET ANALYSIS")
print("=" * 50)

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nEmotion distribution:")
print(df["emotion"].value_counts())

print("\nPercentage distribution:")
print(
    (df["emotion"].value_counts(normalize=True) * 100)
    .round(2)
    .astype(str)
    + "%"
)

print("\nSample examples:")
for emotion in emotion_names.values():
    sample = df[df["emotion"] == emotion].iloc[0]
    print(f"\n{emotion.upper()}:")
    print(sample["text"])

print("\nAnalysis completed.")