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

        self.stt = STT()
        print("STT loaded")
 

    def getSpeech(self, phrase):
        print("STT callback called: " + phrase)
        response = self.llm.generate(phrase)
        print("Response: " + response)
        #self.tts.say(response)

    def start(self):

        while True:
            prompt = None

            def updatePrompt(p):
                print("prompt updated")
                nonlocal prompt 
                prompt = p

            self.stt.listen(updatePrompt)
            seconds = 0
            while not prompt:
                sleep(1)
                seconds += 1
                print("listening for " + str(seconds) + " seconds")
            self.stt.stopListening()
            response = self.llm.generate(prompt)
            print("Response: " + response)
            self.tts.say(response)



def main():
    bot = Chatbot()
    bot.start()

    # stt = STT()
    # stt.listen(lambda p: print("STT callback called: " + p))

    # seconds = 0
    # while True:
    #     sleep(1)
    #     seconds += 1
    #     print(f"Listening for {seconds} seconds")
    

if __name__ == "__main__":
    main()