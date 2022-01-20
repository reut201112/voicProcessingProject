import azure.cognitiveservices.speech as speech

API_KEY = '587664091d7b4e07adbe56251635caef'
ENDPOINT = 'https://eastus.api.cognitive.microsoft.com/sts/v1.0/issuetoken'
file = 'C:\voicProcessingProject\sample1.wav'

transalation_config = speech.translation.SpeechTranslationConfig(
    subscription=API_KEY, endpoint=ENDPOINT)

transalation_config.speech_recognition_language = 'en-US'

audio_config = speech.audio.AudioConfig(filename=file)
recognizer = speech.translation.TranslationRecignizer(
    transalation_config=transalation_config, audio_config=audio_config)

resalts = recognizer.recognize_once()