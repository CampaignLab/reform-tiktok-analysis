import pandas as pd
import subprocess
import os

# Load CSV and extract URLs
CSV_PATH = "data/raw/tiktok_links.csv"
DOWNLOAD_PATH = "downloads/videos/"

df = pd.read_csv(CSV_PATH)
urls = df['mediaUrls/0'].dropna().tolist()

# Create directory for downloaded videos
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# Download each video using yt-dlp
for url in urls:
    try:
        # Construct command to use yt-dlp and download to specific folder
        subprocess.run(['yt-dlp', '-o', f'{DOWNLOAD_PATH}%(title)s.%(ext)s', url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url}: {e}")
