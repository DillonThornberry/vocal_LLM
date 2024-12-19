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

        self.ready = True
 

    def start(self):

        while self.ready:
            prompt = None

            def updatePrompt(p):
                print("prompt updated")
                nonlocal prompt 
                prompt = p

            self.stt.listen(updatePrompt)
            seconds = 0
            while not prompt:
                sleep(.2)
                seconds += .2
                if seconds % 5 == 0:
                    print("listening for " + str(seconds) + " seconds")

            self.stt.stopListening()
            response = self.llm.generate(prompt)
            print("Response: " + response)
            self.tts.say(response)


    def stop(self):
        self.ready = False



def main():
    bot = Chatbot()
    bot.start()
    

if __name__ == "__main__":
    main()