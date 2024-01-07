import cv2
import numpy as np
import scipy.io.wavfile as wav

# Load the encoded audio data
sample_rate, encoded_audio = wav.read('video_encoded_audio.wav')

# Define video dimensions
video_width = 1920
video_height = 1080

# Reshape the encoded audio data to match the original video frames
encoded_frames = np.reshape(encoded_audio, (len(encoded_audio) // (video_width * video_height), -1))

# Create a video file from encoded frames
out = cv2.VideoWriter('output_video_from_audio.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 24, (video_width, video_height))

# Convert frames to uint8 before writing
for frame in encoded_frames:
    frame = cv2.cvtColor(frame.reshape((video_height, video_width)).astype(np.uint8), cv2.COLOR_GRAY2BGR)
    out.write(frame)

out.release()
