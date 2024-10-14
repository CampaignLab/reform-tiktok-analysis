import pandas as pd
from transformers import pipeline

# Load the CSV file
CSV_PATH = "data/raw/tiktok_links.csv"

df = pd.read_csv(CSV_PATH)

# Extract comments or captions column (assuming there's a column named 'caption')
captions = df['caption'].dropna().tolist()

# Initialize sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze each caption
results = []
for caption in captions:
    result = sentiment_analyzer(caption)[0]
    results.append({
        'caption': caption,
        'label': result['label'],
        'score': result['score']
    })

# Save results
OUTPUT_PATH = "analysis/results/sentiment_analysis_results.csv"
sentiment_df = pd.DataFrame(results)
sentiment_df.to_csv(OUTPUT_PATH, index=False)
