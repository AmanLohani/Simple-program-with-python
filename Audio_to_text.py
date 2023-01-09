import speech_recognition as sr
AUDIO_FILE = ("Try_audio.wav")#Only audio file with .wav extension works
#Use audio file as source
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
#Reads aodio file

try:
    print("Audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Audio could not be understood")
except sr.RequestError:
    print("Could not get results")
