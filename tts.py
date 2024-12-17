import pyttsx3



class TTS:

    def __init__(self):
    # Initialize the TTS engine
        self.engine = pyttsx3.init()

        # Set properties
        self.engine.setProperty('rate', 180)  # Speed (default: 200)
        self.engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

        # Choose voice (0: male, 1: female)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # Use female voice         

    def say(self,text):
        # Speak text
        self.engine.say(text)

        # Run the engine
        self.engine.runAndWait()


def main():
    # # Initialize the TTS engine
    # initTTS()

    # # Speak text
    # tts("Hello, world!")

    tts = TTS()
    tts.say("test")


if __name__ == "__main__":
    main()

    