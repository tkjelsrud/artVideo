# Script in python for converting videos into audio and back
# The goal is to approximate analog video synthesis techniques where audio effects can be applied to the (encoded) video signal in order to create various lo-fi effects when returning it to video/mp4 form

# Create audio file using "output_video.mp4" as input
# Output = video_encoded_audio.wav
python3 videoToAudio.py

# Apply any effects to the audio (not tested yet)

# Create video from the audio file
python3 audioToVideo.py  