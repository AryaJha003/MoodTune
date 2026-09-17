from datasets import load_dataset
import pandas as pd
from pathlib import Path

# Load the official split configuration
dataset = load_dataset("dair-ai/emotion", "split")

# Create data directory
data_dir = Path(__file__).resolve().parent.parent / "data"
data_dir.mkdir(exist_ok=True)

# Save each split as CSV
for split_name in ["train", "validation", "test"]:
    df = dataset[split_name].to_pandas()

    output_path = data_dir / f"emotion_{split_name}.csv"
    df.to_csv(output_path, index=False)

    print(f"{split_name}: {len(df)} rows")
    print(f"Saved to: {output_path}")

print("\nEmotion dataset downloaded successfully!")
