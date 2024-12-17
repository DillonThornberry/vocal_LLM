from llm import LLM
from tts import TTS
from stt import STT
from time import sleep

class Chatbot:
    def __init__(self):
        self.llm = LLM()
        print("LLM loaded")
        
        self.tts = TTS()
        print("TTS loaded")

        self.stt = STT(self.getSpeech)
        print("STT loaded with callback")

    def getSpeech(self, phrase):
        print("STT callback called")
        response = self.llm.generate(phrase)
        self.tts.say(response)

    def start(self):
        self.stt.listen()

        seconds = 0
        while True:
            sleep(1)
            seconds += 1
            print("listening for " + str(seconds) + " seconds")


def main():
    bot = Chatbot()
    bot.start()

    

if __name__ == "__main__":
    main()