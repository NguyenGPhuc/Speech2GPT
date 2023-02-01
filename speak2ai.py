import speech_recognition as sr
import openai
from text2speech_config import voice_engine


# Read API key form text file.
### Require your own openai api key ### Create a text file call "api_key.txt" in the same directory. Copy and paste your API key in there and save it.
with open("api_key.txt", "r") as f:
    contents = f.readline().strip()
try:
    # Althernatively, reaplce variable "contents" below with the API key. Exmaple - "123......xyz"
    openai.api_key = contents
except:
    print("Can't read api key from file.")
finally:
    f.close()

# Checks if OpenAI key is valid
try:
    # Try to generate a response using the GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Hello, world!",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print("API key is valid")
except openai.OpenAIError as error:
    print(f"API key is invalid. Error: {error}")

# uses generate text as the generated prompt for ChatGPT
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # return ChatGPT's response
    message = completions.choices[0].text
    return message

# uses text to speech libary to read the reponse
def speech_response(gpt_response):
    voice_engine.say(gpt_response)
    voice_engine.runAndWait()

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

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Ask user if they want Text to speech option. 
voice_question = "Do you want the response read out loud? (yes or no)"
print(voice_question)
speech_response(voice_question)
if (speech_to_text() == "no"):
    voice_option = 0
else:
    voice_option = 1

# program will continuously ask user for a prompt
while True:
        text = speech_to_text()
        print(text)
        if text == 'close chat':
            break

        # enable voiced option while program is running
        elif text == 'voice option on':
            voice_on = "Voice option is now on"
            print(voice_on)
            speech_response(voice_on)
            voice_option = 1
        elif text == 'voice option off':
            if (voice_option != 0):
                voice_off = "Voice option is now off"
                print(voice_off)
                # speech_response(voice_off)
                voice_option = 0
        else:
            print("Promt:" + text)
            response = generate_response(text)

            print(f"Response: {response}\n")

            # text to speech will read the response if enabled
            if (voice_option == 1):
                speech_response(response)        