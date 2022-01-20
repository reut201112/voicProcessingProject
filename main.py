import os
import tkinter

from google.cloud import speech
from tkinter import *

def ress():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'speech-to-text-api-337512-cc480d4f338e.json'
    speech_client = speech.SpeechClient()


    media_url = {'samp1' : 'gs://speech-to-text-medi-files/sample1.wav',
                 'samp2' : 'gs://speech-to-text-medi-files/sample5.wav',
                 'samp3' : 'gs://speech-to-text-medi-files/sample3.wav'
                 }
    for samp in media_url:
        long_audio_wav = speech.RecognitionAudio(uri=media_url.get(samp))

        config_wav_enhance = speech.RecognitionConfig(
            sample_rate_hertz=48000,
            enable_automatic_punctuation=True,
            language_code='en-US',
            use_enhanced=True,
            model='video'
        )

        operation = speech_client.long_running_recognize(
            config=config_wav_enhance,
            audio=long_audio_wav
        )

        response = operation.result(timeout=90)

        for result in response.results:
            split = str(result.alternatives[0].transcript)
            dict = split.split()
            index = 1
            for index,word in enumerate(dict):
                if dict[index] == dict[index-1]:
                    del dict[index]
            stri = " ".join(dict)
            stri = stri.replace(".",".\n")
            text.insert(tkinter.INSERT,stri)
            text.insert(tkinter.INSERT, "\n")


window = Tk()
text = Text(window)
text.pack()
button = Button(window,text="transcript",command=ress)
button.pack()
window.mainloop()