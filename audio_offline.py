import speech_recognition as sr
import subprocess
from os import path
import requests
import markovify

# OFFLINE VERSION OF AUDIO RECOGNITION SCRIPT
# FFMPEG MUST BE INSTALLED. RUN brew install ffmpeg ON A MAC.

# ↓ name of video file goes here ↓
my_video_file = "southpark.mp4"
my_audio_file = "output-audio.aac"
my_wav_file = my_audio_file.replace("aac", "wav")
ffmpeg_command = f"ffmpeg -i {my_video_file} -vn -acodec copy {my_audio_file}".split(" ")

subprocess.call(ffmpeg_command)
subprocess.call(["ffmpeg", "-i", my_audio_file, my_wav_file])

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), my_wav_file)
print(AUDIO_FILE)

r = sr.Recognizer()
# m = sr.Microphone()
# with m as source:
#     r.adjust_for_ambient_noise()
"""
# stop = r.listen_i
with sr.Microphone() as source:
    print("Say something!")
    # audio = r.listen(source)
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    audio = r.record(source, duration=10)

try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
"""

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
try:
    output=r.recognize_sphinx(audio)
    print(output)
    # uncomment the below once the server is up
    """
    rq = requests.post("server_url_here", data={"text:" output})
    """
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

with open("output.txt", 'w') as f:
    f.write(output)

text_model = markovify.Text(output)

for i in range(5):
    print(text_model.make_sentence())

# for later maybe
# write audio to a RAW file
#with open("microphone-results.raw", "wb") as f:
#  f.write(audio.get_raw_data())

# need to get file f and transcribe



