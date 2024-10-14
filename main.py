import subprocess

# Run download videos script
subprocess.run(['python', 'analysis/scripts/download_videos.py'])

# Run extract audio script
subprocess.run(['python', 'analysis/scripts/extract_audio.py'])

# Run video analysis script
subprocess.run(['python', 'analysis/scripts/video_analysis.py'])

# Run sentiment analysis script
subprocess.run(['python', 'analysis/scripts/sentiment_analysis.py'])
