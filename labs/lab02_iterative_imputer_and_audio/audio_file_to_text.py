import speech_recognition as sr
from global_constants import PATH
PATH = f"{PATH}audiosamples1/elaine_0.wav"

r = sr.Recognizer()

audioFile = sr.AudioFile(PATH)
with audioFile as source:
    audio  = r.record(source)
    output = r.recognize_google(audio)
    print(output)
