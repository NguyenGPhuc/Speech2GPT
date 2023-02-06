import os
import openai

# Read API key form text file.
### Require your own openai api key ### Create a text file call "api_key.txt" in the same directory. Copy and paste your API key in there and save it.
with open("api_key.txt", "r") as f:
    contents = f.readline().strip()
try:
    # Althernatively, reaplce variable "contents" below with the API key. Exmaple - "123......xyz"
    openai.api_key = contents
    # openai.api_key = os.getenv(contents)
except:
    print("Can't read api key from file.")
finally:
    f.close()

# uses generate text as the generated prompt for ChatGPT
def generate_response(author, theme, text):
    try:
        # AI modification of text base on user specification
        if author != 'None' and theme != 'None' and text != '':
            prompt = "Rewrite this passage in a similar style to " + author + "in a " + theme + " theme :" + text
        elif author == 'None' and theme != 'None' and text != '':
            prompt = "Rewrite this passge in a " + theme + " theme: " + text
        elif author != 'None' and theme == 'None' and text != '':
            prompt = "Rewrite this passage in a similar style to author " + author + ": " + text
        
        # if no specification selected, AI will just fix grammar
        elif text != '' and author == 'None' and theme == 'None': 
            prompt="Correct this if it has any grammar issues, else leave it the same: " + text,

        # AI generated story when there's no user input.
        elif text != '' and author != 'None' and theme == 'None':
            prompt = "Write a short one paragraph story similar to author " + author + " style of writing"
        
        elif text != '' and author == 'None' and theme != 'None':
            prompt = "Write a short one paragraph story with " + theme + " Theme"
        else:
            print("Generate random story")
            prompt = "Write a short one paragraph story about anything."
        
        completions = openai.Completion.create(
            # engine="text-davinci-002",
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=512,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # return ChatGPT's response
        message = completions.choices[0].text
        return message
    # Returns error if API key is invalid
    except openai.OpenAIError as error:
        print(f"API key is invalid. Error: {error}")
        

    # # return ChatGPT's response
    # message = completions.choices[0].text
    # return message

    
        