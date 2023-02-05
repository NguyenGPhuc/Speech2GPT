from text2speech import *
from openai_service import *
from speech2text import *
from writing_log import *
from command_option import *


current_paragraph = ''
current_page = ''
current_book = ''

paragraph_num = 1
page_num = 1
book_num = 1

# program will continuously ask user for a prompt
while True:
        # reading from speech-to-text
        # text_speech = speech_to_text()
        print('Main Menu')
        print('Say...')
        print('"writing mode" to start wrting by verbally tells your story.\n')
        print('"ask ai" interact with an AI that will generate response base on user given prompt.\n')
        print('"modify paragraph" to make edit to current paragraph. This can be grammar check, theme change or so on\n')
        print('"modify page" to make changes to the current page. This can be grammar check, theme change or so on\n')
        print('"read book" to display the currently book in its finish form.\n')
        command = speech_to_text()

        # reading from user keyboard input
        # text_input = input('Write or say a promt\n')
        # command = input('Start writing or say a command\n')
        current_passage = ''

        # program will close upon hearing "close chat" or "end chat"
        if command_line(command) == 'terminate':
            break


        else:
            # checks to see if speech was successfully converted to text
            if command != "Sorry, I did not get that":        
                # if user want to ask openAI to do something instead of writing.
                if command_line(command) == 'ask ai':
                    while True:
                        print('Ask AI anything ヽ(ヅ)ノ')
                        command = speech_to_text()

                        # program will close upon hearing "close chat" or "end chat"
                        if command_line(command) == 'close ai':
                            break
                        
                        response = generate_response(command)
                        print(f"Response: {response}\n\n")
                        
                        print("Would you like to overwrite what you've written with AI generated response?")
                        # overwrite user passage with AI generated resonse.
                        if speech_to_text() == 'yes':
                            write_log(response)

                # simply record speech to text log.
                else:
                    current_passage = command + '. '
                    current_paragraph = '. ' + current_passage
                    print('Currently have: ' + current_paragraph)


                    
            else:
                print("Sorry, I did not get that") 

