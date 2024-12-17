import speech_recognition as sr
import pyaudio
from time import sleep

class STT:

    def __init__(self, callback=None):
        self.p = pyaudio.PyAudio()

        if callback:
            self.listenCallback = callback
            print("STT initialized with callback")

        self.deviceIndex = -1
        for i in range(self.p.get_device_count()):
            device = self.p.get_device_info_by_index(i)

            if device['name'] == 'Microphone (Scarlett 2i2 USB)':
                self.deviceIndex = i
                print("Found microphone at index", i)
                break

    listenCallback = None
    
    def defaultListenCallback(self, recognizer, audio):                          # this is called from the background thread
        try:
            phrase = recognizer.recognize_google(audio)
            print("You said " + phrase)  # received audio data, now need to recognize it
            if self.listenCallback:
                self.listenCallback(phrase)
                print("Callback called")
                self.stopListening()
                print("Listening stopped")
                self.listen()
                print("Listening restarted")

        except LookupError:
            print("Oops! Didn't catch that")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")

    def listen(self):
        r = sr.Recognizer()
        m = sr.Microphone(device_index=self.deviceIndex)
        with m as source: r.adjust_for_ambient_noise(source)      # we only need to calibrate once, before we start listening
        self.killListener = r.listen_in_background(m, self.defaultListenCallback)
        print("Listening...")

    def stopListening(self):
        if self.killListener:
            self.killListener()
            self.killListener = None

        else:
            print("No listener to stop")

def main():
    stt = STT()
    stt.listen()

    seconds = 0
    while True:
        sleep(1)
        seconds += 1
        print(f"Listening for {seconds} seconds")

    # sleep(10)
    # stt.stopListening()

if __name__ == "__main__": 
    main()