import speech_recognition as sr

r = sr.Recognizer()
# m = sr.Microphone()
# with m as source:
#     r.adjust_for_ambient_noise()

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

## recognize speech using Google Speech Recognition
try:
    output=r.recognize_google(audio)
    print(output)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


# for later maybe
# write audio to a RAW file
#with open("microphone-results.raw", "wb") as f:
#  f.write(audio.get_raw_data())

# need to get file f and transcribe






