import speech_recognition as sr

# Read API key form text file.
with open("api_key.txt", "r") as f:
    contents= f.readlines()

try: 
    print(contents)

except:
    print("Can't read api key from file.")

finally:
    f.close()

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Recording started")
    audio = r.listen(source)
    print("Recording ended")
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
try:
    # using google speech recognition
    # print("Working!")

    text = r.recognize_google(audio)
    print("Text:" + text)
except:
    print("Sorry, I did not get that")