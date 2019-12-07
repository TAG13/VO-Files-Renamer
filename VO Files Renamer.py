#variables
prefix = ''
suffix = ''
fileNameLength = 50
camelCase = True

"""
Quick Instructions:
Place this Python file in the same folder as the audio files you want to rename.

Adjust the variables above as needed for you project.
For the prefix and suffix variables, be sure to include
    apostrophes or quotation marks at the beginning and
    end of your values. For example:
    prefix = 'Narrator_'
    If you don't want a prefix or a suffix, simply set the variable
    as two apostrophes or two quotation marks. For example:
    prefix = ""
FileNameLength is used to limit the size of your file name,
    measured in characters.
    This variable does not take into account the prefix or suffix.
If camelCase is set to True, then each word will be
    capitalized and all spaces removed. For example:
    "How are you.wav" becomes "HowAreYou.wav"

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

import speech_recognition as sr
import string
import os
import urllib.error
from pprint import pprint
from os import path

i = 0

for filename in os.listdir():
    if filename.endswith((".wav", ".flac", ".aiff", ".aif")): #endswith can accept tuples
        #saves the file extension
        origName = filename
        ext = os.path.splitext (filename)[1] #splitext splits the root from the extension. [0] is root, [1] is extension.
        try:
            AUDIO_FILE = os.path.join(path.dirname(path.realpath(__file__)), filename)
            r = sr.Recognizer()
            unnamed = sr.AudioFile(filename)
            with unnamed as source:
                audio = r.record(source)
            #sends the text off to Google's elves. Requires internet connection. 
            text = r.recognize_google(audio)

            #variables for naming rules
            if camelCase == True:
                #string.capwords capitalizes the first character of every word in a string
                text = (string.capwords (text))
                # removing all the spaces
                text = text.replace(" ", "")

            #Slicing the string. Limiting the string to fileNameLength
            text = text[0:(fileNameLength +1)]

            pprint (origName + " --> " + prefix + text + suffix + ext)
            os.rename (filename, prefix + text + suffix + ext)

            
        #error handling
        except FileNotFoundError:
            pprint ("Could not find the file to rename. Try renaming the file to \"01.wav\"")

        except urllib.error.HTTPError:
            pprint ("Speech-to-text failed on " + filename + ". Is this file a clean recording of spoken dialog? Is your file under 60 seconds long? Is your internet connection working?")

        except sr.RequestError as e:
            pprint (filename + " failed. Speech-to-text was not able to understand this audio. Is this file a clean recording of spoken dialog? Is your file under 60 seconds long? Is your internet connection working?")

        except PermissionError:
            pprint(filename + " failed. Do you have this file open in another program?")

    elif filename.endswith((".ogg", ".mp3", ".aac", ".wma")):
        pprint(filename + " cannot not be analyzed. The speech-to-text process only supports .wav, .flac, and .aiff files.")

    i += 1  

pprint ('Done!')
