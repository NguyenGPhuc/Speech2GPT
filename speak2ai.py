from openai_service import *
from speech2text import *
from writing_log import *
from command_option import *
import tkinter as tk
from tkinter import Label
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk



current_paragraph = ''
current_page = ''
current_book = ''

paragraph_num = 1
page_num = 1
book_num = 1

# Python handle dropdown menu
def drop_down():
    selected_option = dropdown_var.get()
    print(f"Button clicked. Selected option: {selected_option}.")

# record user input
def save_input():
    global user_input
    user_input = text_box.get("1.0", "end")

window = tk.Tk()
window.title("Story Squire")
window.geometry("680x900")


# Create drop down menu
options = ["Option 1", "Option 2", "Option 3"]
dropdown_var = tk.StringVar()
dropdown_var.set(options[0])
dropdown = tk.OptionMenu(window, dropdown_var, *options)
dropdown.pack()

# Create text box where user write their story
text_box = tk.Text(window, width=20, height=40, font="Time 12")
text_box.pack()

# Create button
button = tk.Button(window, text="Save", command=save_input)
button.pack()

window.mainloop()

print(f"User input: {user_input}")


# # program will continuously ask user for a prompt
# while True:
#         # reading from speech-to-text
#         # text_speech = speech_to_text()
#         # print('Main Menu')
#         # print('Say...')
#         # print('"writing mode" to start wrting by verbally tells your story.\n')
#         # # print('"ask ai" interact with an AI that will generate response base on user given prompt.\n')
#         # print('"modify paragraph" to make edit to current paragraph. This can be grammar check, theme change or so on\n')
#         # print('"modify page" to make changes to the current page. This can be grammar check, theme change or so on\n')
#         # print('"read book" to display the currently book in its finish form.\n')
#         promt = speech_to_text()

#         # reading from user keyboard input
#         # text_input = input('Write or say a promt\n')
#         # promt = input('Start writing or say a promt\n')
#         current_passage = ''

#         # program will close upon hearing "close chat" or "end chat"
#         if command_line(promt) == 'terminate':
#             break


#         else:
#             # checks to see if speech was successfully converted to text
#             if promt != "Sorry, I did not get that":
#                 # simply record speech to text log.
#                 if command_line(promt) == 'writing mode':
#                     while True:
#                         # exit writing mode
#                         if command_line(promt) == 'close writing':
#                             break
#                         else:
#                             print('Start recording your story by speaking into the mic')
#                             promt = speech_to_text()
#                             if command_line(promt) == 'ask ai':
#                                 print('Ask AI anything')
#                                 promt = speech_to_text()

#                                 # program will close upon hearing "close chat" or "end chat"
#                                 if command_line(promt) == 'close ai':
#                                     break
                                
#                                 response = generate_response(promt)
#                                 print(f"Response: {response}\n\n")
                                
#                                 print("Would you like to overwrite what you've written with AI generated response?")
#                                 # overwrite user passage with AI generated resonse.
#                                 if speech_to_text() == 'yes':
#                                     write_log(response)

#                             # basic speech to text writing mode
#                             else:
#                                 current_passage = promt + '. '

#                                 current_paragraph = '. ' + current_passage

#                                 print('Currently have: ' + current_paragraph)
#                                 current_paragraph = check_grammar(current_paragraph)
#                                 print('Currently have (grammar checked): ' + current_paragraph)

#                 # if user want to ask openAI to do something instead of writing.
#                 if command_line(promt) == 'ask ai':
            
#                     print('Ask AI anything ヽ(ヅ)ノ')
#                     promt = speech_to_text()

#                     # program will close upon hearing "close chat" or "end chat"
#                     if command_line(promt) == 'close ai':
#                         break
                    
#                     response = generate_response(promt)
#                     print(f"Response: {response}\n\n")
                    
#                     print("Would you like to overwrite what you've written with AI generated response?")
#                     # overwrite user passage with AI generated resonse.
#                     if speech_to_text() == 'yes':
#                         write_log(response)
                    
#             else:
#                 print("Sorry, I did not get that") 