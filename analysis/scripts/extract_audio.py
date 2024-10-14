import os
import moviepy.editor as mp

VIDEOS_PATH = "downloads/videos/"
AUDIO_OUTPUT_PATH = "data/processed/audio/"

# Create output folder if it doesn't exist
os.makedirs(AUDIO_OUTPUT_PATH, exist_ok=True)

# Loop through all video files and extract audio
for filename in os.listdir(VIDEOS_PATH):
    if filename.endswith((".mp4", ".webm")):
        video_path = os.path.join(VIDEOS_PATH, filename)
        audio_filename = os.path.splitext(filename)[0] + ".wav"
        audio_output_path = os.path.join(AUDIO_OUTPUT_PATH, audio_filename)

        # Extract audio using moviepy
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(audio_output_path)
