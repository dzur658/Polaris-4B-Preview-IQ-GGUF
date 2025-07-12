from datasets import load_dataset
from collections import Counter
import pandas as pd

# --- Configuration ---
DATASET_NAME = "POLARIS-Project/Polaris-Dataset-53K"
SPLIT_NAME = "train"
STRATIFY_COLUMN = "difficulty"
SAMPLE_SIZE = 10000
OUTPUT_FILE = "polaris-calibration.txt"
RANDOM_SEED = 42

print(f"⬇️  Loading dataset '{DATASET_NAME}'...")
dataset = load_dataset(DATASET_NAME, split=SPLIT_NAME)

print(f"Performing stratified sampling based on '{STRATIFY_COLUMN}'...")

# Convert to pandas for easier stratified sampling
df = dataset.to_pandas()

# Perform stratified sampling
# This ensures the sample has the same distribution of 'difficulty' as the original dataset
stratified_sample_df = df.groupby(STRATIFY_COLUMN, group_keys=False).apply(
    lambda x: x.sample(frac=min(SAMPLE_SIZE / len(df), 1.0), random_state=RANDOM_SEED)
)

# If the frac method gives us slightly more or less, we'll take a final random sample to get the exact size
if len(stratified_sample_df) != SAMPLE_SIZE:
     stratified_sample_df = stratified_sample_df.sample(n=SAMPLE_SIZE, random_state=RANDOM_SEED)


print(f"⏳  Processing {len(stratified_sample_df)} samples to create calibration file...")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for _, row in stratified_sample_df.iterrows():
        # Recreate the Qwen2 / ChatML prompt format that Polaris uses.
        text = f"<|im_start|>user\n{row['problem']}<|im_end|>\n<|im_start|>assistant\n{row['answer']}<|im_end|>\n"
        f.write(text)
        print(f"📝  writing in progress...")

print(f"✅  Stratified calibration data has been successfully written to '{OUTPUT_FILE}'")