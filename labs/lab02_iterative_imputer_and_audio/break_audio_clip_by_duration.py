import speech_recognition as sr
from global_constants import PATH
PATH = f"{PATH}/audiosamples1/kramer_3.wav"

r = sr.Recognizer()

jackhammer = sr.AudioFile(PATH)
with jackhammer as source:
    audio1 = r.record(source, duration=1.5)
    audio2 = r.record(source, duration=1.2)

    # Shows first section.
    output1 = r.recognize_google(audio1)
    print(output1)

    # Shows second section.
    output2 = r.recognize_google(audio2)
    print(output2)
