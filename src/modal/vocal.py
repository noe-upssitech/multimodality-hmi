import speech_recognition as sr

class Vocal:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self) -> str:
        with self.microphone as source:
            print("Where do you wish to go ?")
            print("Waiting for your answer...")
            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)

        try:
            text = self.recognizer.recognize_google(audio, language="en-EN")
            print("I understood: " + text)
            return text
        except sr.UnknownValueError:
            print("I did not understand")
            return None
        except sr.RequestError as e:
            print("Error: ".format(e))
            return None

    def interpret(self, text: str) -> int:
        if text is None:
            return None
        
        text = text.lower()

        if "school" in text:
            return 26
        if "university" in text:
            return 18
        if "library" in text:
            return 38
        if "cinema" in text:
            return 7
        if "bus" in text or "station" in text:
            return 28
        if "train" in text:
            return 23
        if "mall" in text:
            return 7
        if "post" in text or "office" in text:
            return 30
        if "park" in text:
            return 32
        if "home" in text:
            return 1
        else:
            return None
        

if __name__ == "__main__":
    vocal = Vocal()
    id = vocal.interpret(vocal.listen())
    print(id)