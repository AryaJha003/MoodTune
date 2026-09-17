from datasets import load_dataset
from pathlib import Path

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

print("Downloading Spotify Tracks Dataset...")

# Load dataset
dataset = load_dataset(
    "maharshipandya/spotify-tracks-dataset"
)

# Get the training split
df = dataset["train"].to_pandas()

print(f"Downloaded {len(df)} tracks.")
print(f"Columns: {list(df.columns)}")

# Save locally
output_path = DATA_DIR / "spotify_tracks.csv"

df.to_csv(output_path, index=False)

print(f"\nSaved to:")
print(output_path)

print("\nMusic dataset downloaded successfully!")