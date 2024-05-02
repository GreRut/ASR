from speech_recogniser import SpeechRecognizer

speech_recognizer = SpeechRecognizer()
text = speech_recognizer.recognize_speech_from_mic()
if text:
    print("You said:", text)
