import speech_recognition as sr

r = sr.Recognizer()

sample = sr.AudioFile('sample1.wav')
with sample as source:
    audio=r.record(source)
print(r.recognize_google(audio))