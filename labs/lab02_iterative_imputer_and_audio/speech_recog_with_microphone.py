import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    # Add the following line to filter out background noise.
    # r.adjust_for_ambient_noise(source)
    text = ""
    while text != "stop":
        audio = r.listen(source)
        text = r.recognize_google(audio, language='en-IN')
        print(text)
# output = r.recognize_google(audio)


