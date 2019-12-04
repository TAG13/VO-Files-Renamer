#variables
prefix = 'prefix-test_'
suffix = '_suffix-test'
fileNameLength = 50
camelCase = True

"""
Quick Instructions:
Adjust the variables above as needed for you project.
For the prefix and suffix variables, be sure to include
    apostrophes or quotation marks at the beginning and
    end of your values. For example:
    prefix = 'Narrator_'
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

#trying to batch rename files over here

"""
def main(): 
    i = 0
      
    for filename in os.path.join(path.dirname(path.realpath(__file__)), file):
        #AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")
        file = filename
        r = sr.Recognizer()
        with sr.file as source:
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

try:
    # obtain path to "01.wav" in the same folder as this script
    from os import path
    AUDIO_FILE = os.path.join(path.dirname(path.realpath(__file__)), "01.wav")

    r = sr.Recognizer()

    unnamed = sr.AudioFile('01.wav')
    with unnamed as source:
        audio = r.record(source)
    #sends the text off to Google's elves. Requires internet connection. 
    text = r.recognize_google(audio)

    if camelCase == True:
        #string.capwords capitalizes the first character of every word in a string
        text = (string.capwords (text))

        # .replace is used here to remove all the spaces
        text = text.replace(" ", "")

    #Slicing the string. Limiting the string to 50 characters
    text = text[0:(fileNameLength +1)]

    print (prefix + text + suffix)

    os.rename ('01.wav', prefix + text + suffix + '.wav')

    print ('Done!')

#error handling
except FileNotFoundError:
    print ("Could not find the file to rename. Try renaming the file to \"01.wav\"")

except urllib.error.HTTPError:
    print ("Speech-to-text failed. Is the file a clean recording of spoken dialog? Is your file under a 60 seconds long? Is your internet connection working?")

except sr.RequestError as e:
    print ("Speech-to-text failed. Is the file a clean recording of spoken dialog? Is your file under a 60 seconds long? Is your internet connection working?")
