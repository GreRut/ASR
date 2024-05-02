import speech_recognition as sr

class SpeechRecognizer:
    """
    A class to perform automatic speech recognition (ASR) using the speech_recognition library.
    """

    def __init__(self):
        """
        Initialize the SpeechRecognizer object.
        """
        self.recognizer = sr.Recognizer()

    def recognize_speech_from_mic(self):
        """
        Recognizes speech from the microphone.

        Returns:
            str or None: The recognized text if successful, otherwise None.
        """
        with sr.Microphone() as source:
            print("Say something...")
            self.recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            # Using Sphinx recognizer for offline recognition
            recognized_text = self.recognizer.recognize_sphinx(audio)
            return recognized_text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return None
        except sr.RequestError as e:
            print(f"Error: {e}")
            return None