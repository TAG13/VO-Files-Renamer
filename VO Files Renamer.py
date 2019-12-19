#variables
prefix = 'prefix-test_'
suffix = '_suffix-test'
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
from os import path

#Can be ignored if you're not using your own Google Cloud Speech key.
google_cloud_credential = r"""PASTE THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""

i = 0

for filename in os.listdir():
    if filename.endswith(".wav" or ".flac" or ".aiff"):
        #saves the file extension
        ext = os.path.splitext (filename)[1]
        original = filename
        try:
            AUDIO_FILE = os.path.join(path.dirname(path.realpath(__file__)), filename)
            r = sr.Recognizer()
            unnamed = sr.AudioFile(filename)
            with unnamed as source:
                audio = r.record(source)
                
            #=== Send the text off to Google's elves. Requires internet connection. === 
            #default api key. Just works. Good for testing.
            text = r.recognize_google(audio)
                
            #Google Cloud Speech. Need your own credential key from Google.
            #text = r.recognize_google_cloud(audio, credentials_json = google_cloud_credential)
                        
            #variables for naming rules
            if camelCase == True:
                #string.capwords capitalizes the first character of every word in a string
                text = (string.capwords (text))
                # removing all the spaces
                text = text.replace(" ", "")

            #Slicing the string. Limiting the string to fileNameLength
            text = text[0:(fileNameLength +1)]

            print (original + " --> " + prefix + text + suffix)
            os.rename (filename, prefix + text + suffix + ext)

            
        #error handling

        except sr.UnknownValueError:
            print (filename + " speech-to-text failed. Is this file a clean recording of spoken dialog? Is your file under a 60 seconds long? Is your internet connection working?")

        except urllib.error.HTTPError:
            print (filename + " speech-to-text failed. Is this file a clean recording of spoken dialog? Is your file under a 60 seconds long? Is your internet connection working?")

        except sr.RequestError as e:
            print ((filename + " speech-to-text failed. Could not request results from Google Cloud Speech service; {0}".format(e)))

        #HACKY!!
        #If you try to open a folder instead a file, this error is thrown.
        #Better solution is to differentiate between files and folders.
        except PermissionError:
            print("")

        i += 1  

print ('Done!')
