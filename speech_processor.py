import speech_recognition as sr


class SpeechProcessing:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Hamura is Listening..")
            audio = None
           
            try:
                audio = self.recognizer.listen(source, timeout=10)
            except sr.WaitTimeoutError:
                print("Listening timeout error")
            
            text = ""

            try:
                print("Recognizing..")
                text = self.recognizer.recognize_google(audio)
                print(f"User said: {text}")
            except sr.UnknownValueError:
                print ("Hamura could not recognize audio")
            except sr.RequestError:
                print("could not request results")
            except Exception:
                print("There was an exception error")

            return text
        
    def speak(self):
        pass


