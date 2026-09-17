import pandas as pd
from pathlib import Path

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load dataset
df = pd.read_csv(DATA_DIR / "spotify_tracks.csv")

print("=" * 60)
print("MOODTUNE - MUSIC DATASET ANALYSIS")
print("=" * 60)

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

print("\nSample songs:")
print(
    df[
        [
            "track_name",
            "artists",
            "track_genre",
            "danceability",
            "energy",
            "valence",
            "acousticness",
            "tempo"
        ]
    ].head(10).to_string(index=False)
)

print("\nGenre count:")
print(df["track_genre"].nunique())

print("\nNumber of tracks per genre:")
print(df["track_genre"].value_counts().head(15))

print("\nMusic dataset analysis completed!")