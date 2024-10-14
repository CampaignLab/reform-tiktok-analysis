import os
import cv2

VIDEOS_PATH = "downloads/videos/"
FRAMES_OUTPUT_PATH = "analysis/results/video_frames/"

# Create output folder if it doesn't exist
os.makedirs(FRAMES_OUTPUT_PATH, exist_ok=True)

# Loop through all video files and extract frames
for filename in os.listdir(VIDEOS_PATH):
    if filename.endswith((".mp4", ".webm")):
        video_path = os.path.join(VIDEOS_PATH, filename)
        video = cv2.VideoCapture(video_path)

        frame_idx = 0
        while True:
            ret, frame = video.read()
            if not ret:
                break

            # Save every 30th frame (i.e., one frame per second for 30 FPS videos)
            if frame_idx % 30 == 0:
                frame_filename = f"{os.path.splitext(filename)[0]}_frame_{frame_idx}.jpg"
                frame_path = os.path.join(FRAMES_OUTPUT_PATH, frame_filename)
                cv2.imwrite(frame_path, frame)

            frame_idx += 1

        video.release()
