import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Say or ask something")
    audio = r.listen(source)
    print("Speech period ended")
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
try:
    # using google speech recognition
    # print("Working!")

    text = r.recognize_google(audio)
    print("Text:" + text)
except:
    print("Sorry, I did not get that")