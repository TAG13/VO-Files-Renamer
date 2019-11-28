import speech_recognition as sr
import string
import os

"""
this program uses Google Web Speech API

"Caution: The default key provided by SpeechRecognition is for
testing purposes only, and Google may revoke it at any time.
It is not a good idea to use the Google Web Speech API in production.
Even with a valid API key, you’ll be limited to only 50 requests per day,
and there is no way to raise this quota.
Fortunately, SpeechRecognition’s interface is nearly identical for each API,
so what you learn today will be easy to translate to a real-world project."

Alternative options:

    recognize_bing(): Microsoft Bing Speech
    recognize_google(): Google Web Speech API
    recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
    recognize_houndify(): Houndify by SoundHound
    recognize_ibm(): IBM Speech to Text
    recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
    recognize_wit(): Wit.ai

https://realpython.com/python-speech-recognition/
"""
print (sr.__version__)


"""
#trying to batch rename files over here
def main(): 
    i = 1
      
    for filename in os.listdir("audio_files"): 
        i = sr.AudioFile(str(i) + '.wav')
        with i as source:
            audio = r.record(source)
        #sends the text off to Google's elves. Requires internet connection. 
        text = r.recognize_google(audio)

        #string.capwords capitalizes the first character of every word in a string
        text = (string.capwords (text))

        # .replace is used here to remove all the spaces
        text = text.replace(" ", "")

        dst = text + ".wav"
        src ='audio_files' + filename 
        dst ='audio_files' + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1

# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()
    """



# obtain path to "unnamed.wav" in the same folder as this script
from os import path
AUDIO_FILE = os.path.join(path.dirname(path.realpath(__file__)), "unnamed.wav")

r = sr.Recognizer()

unnamed = sr.AudioFile('unnamed.wav')
with unnamed as source:
    audio = r.record(source)
#sends the text off to Google's elves. Requires internet connection. 
text = r.recognize_google(audio)

#string.capwords capitalizes the first character of every word in a string
text = (string.capwords (text))

# .replace is used here to remove all the spaces
text = text.replace(" ", "")

#Slicing the string. Limiting the string to 50 characters
text = text[0:51]

print (text)

os.rename ('unnamed.wav', text + '.wav')

