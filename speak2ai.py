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
        # engine="text-davinci-002",
        engine="text-ada-001",
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
        # engine="text-davinci-002",
        engine="text-ada-001",
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.5,
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

# # Ask user if they want Text to speech option. 
# voice_question = "Do you want the response read out loud? (yes or no)"
# print(voice_question)
voice_option = 0
# speech_response(voice_question)
# if (speech_to_text() == "no"):
#     voice_option = 0
# else:
#     voice_option = 1

# Ask user if they want to create an output file
log_option = input("Do you want to record the prompt and response? (Y/N)")
if log_option.lower() == 'y' or log_option.lower() == "yes":
    log = 1
else:
    log = 0
    

# program will continuously ask user for a prompt
while True:
        # reading from speech-to-text
        # text = speech_to_text()

        # reading from user keyboard input
        text = input('Write a prompt\n')
        
        # write prompt to file if log option is enabled.
        print("Prompt: " + text)
        if log == 1:
            f = open("temp.txt", 'w')
            f.write("Prompt: " + text)
            f.close()

        # program will close upon hearing "close chat" or "end chat"
        if text == 'close chat' or text == 'end chat':
            break

        # enable voiced option while program is running by saying "voice option ON"
        elif text == 'voice option on':
            if voice_option != 1:
                voice_on = "Voice option is now on"
                print(voice_on)
                speech_response(voice_on)
                voice_option = 1
        # diable voiced option while program is running by saying "voice option OFF"
        elif text == 'voice option off':
            if voice_option != 0:
                voice_off = "Voice option is now off"
                print(voice_off)
                # speech_response(voice_off)
                voice_option = 0
        else:
            # checks to see if speech was successfully converted to text
            print(text)
            if text != "Sorry, I did not get that":
                response = generate_response(text)
            else:
                print(text) 

            print(f"Response: {response}\n")

            print("Do you want to record this response? (Y/N)")
            

            # text to speech will read the response if enabled
            if (voice_option == 1):
                speech_response(response)        