import streamlit as st
import numpy as np
from PIL import Image

st.write('### :violet[image]')

image = Image.open('flower.jpg')
st.image(image, caption='The beautiful flower')

st.code('''
from PIL import Image
image = Image.open('flower.jpg')
st.image(image, caption='The beautiful flower')
        ''')

st.write('### :violet[audio]')

audio_file = open('sample.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)

st.code('''
import numpy as np
        
audio_file = open('sample.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)
        
''')

st.write('### :violet[video]')

video_file = open('video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
