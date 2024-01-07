import numpy as np
import scipy.io.wavfile as wav
import cv2

# Video file path
video_path = 'your_video.mp4'

# Read video to get the duration (in seconds)
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count / fps
cap.release()



# Create a silent audio track
#sample_rate = 48000  # Adjust as needed
#duration_samples = int(duration * sample_rate)
#silent_audio = np.zeros(duration_samples, dtype=np.int16)

# Save the silent audio track
#wav.write('silent_audio.wav', sample_rate, silent_audio)


# Read video to get the duration (in seconds) and frame information
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.release()

print(f"Processing: fps {fps} frames {frame_count} w {video_width} h {video_height}")

# Calculate total number of samples in the audio
total_samples = int(frame_count * video_width * video_height)

# Create an array to store the audio samples
audio_samples = np.zeros(total_samples, dtype=np.int16)

# Read each frame and encode pixel values into audio samples
cap = cv2.VideoCapture(video_path)
frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flatten the frame array and reshape to match the intended shape
    flattened_frame = frame.flatten()
    flattened_frame = flattened_frame[:video_width * video_height]  # Ensure the correct size
    audio_samples[frame_number * video_width * video_height: (frame_number + 1) * video_width * video_height] = flattened_frame

    frame_number += 1

cap.release()

# Scale the audio samples to increase volume
scaling_factor = 5.0  # Adjust as needed
audio_samples = (audio_samples * scaling_factor).astype(np.int16)

# Save the encoded audio
wav.write('video_encoded_audio.wav', int(fps), audio_samples)
