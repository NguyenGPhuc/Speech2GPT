import speech_recognition as sr
import openai

# Read API key form text file.
### Require your own openai api key ### Create a text file call "api_key.txt" in the same directory. Copy and paste your API key in there and save it.
with open("api_key.txt", "r") as f:
    contents = f.readline().strip()
try:
    # Althernatively, reaplce varible "contents" below with the API key. Exmaple - "123......xyz"
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
    # using google speech recognition to translate into text
    # print("Working!")
    text = r.recognize_google(audio)
    print("Promt: " + text)

    # uses generate text as the prompt for ChatGPT
    prompt = text

    # Generate a response using the GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the ChatGPT's response
    # print("Response: " + response["choices"][0]["text"])
    print("Response: " + response["choices"][0]["text"])
except:
    print("Sorry, I did not get that")