import cv2
import numpy as np
import scipy.io.wavfile as wav

# Load the encoded audio data
sample_rate, encoded_audio = wav.read('video_encoded_audio.wav')

# Define video dimensions
video_width = 1920
video_height = 1080

# Calculate the number of audio samples per video frame
samples_per_frame = video_width * video_height

# Reshape the encoded audio data based on the number of samples per frame
try:
    encoded_frames = np.reshape(encoded_audio, (encoded_audio.size // samples_per_frame, samples_per_frame))
except ValueError as e:
    print(f"Error during reshaping: {e}")
    exit(1)  # Exit the script if there's an error

# Create a video file from encoded frames
out = cv2.VideoWriter('output_video_from_audio.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 24, (video_width, video_height))

# Convert frames to uint8 before writing
for frame_number, frame in enumerate(encoded_frames):
    try:
        frame = cv2.cvtColor(frame.reshape((video_height, video_width)).astype(np.uint8), cv2.COLOR_GRAY2BGR)
        out.write(frame)
    except ValueError as e:
        print(f"Error processing frame {frame_number}: {e}")

out.release()
