
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# creates plain text using user speech
def speech_to_text():
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Recording ended\n")
    try:
        # using google speech recognition to translate into text
        # print("Working!")
        convert_text = r.recognize_google(audio)
      
    except:
        convert_text = "Sorry, I did not get that"
    finally:
        return convert_text