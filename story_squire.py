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

# drop down menu for authors
def update_dropdown():
    global chosen_author
    selected_author = author_var.get()
    if selected_author == "None":
        chosen_author = "no"
    else:
        chosen_author = selected_author

    global chosen_theme
    selected_theme = theme_var.get()
    if selected_theme == "None":
        chosen_theme = "no"
    else:
        chosen_theme =  selected_theme
    

    label.config(text="You have chosen [ " + chosen_author + " ] style with [ " + chosen_theme + " ] theme.")
    print(f"Selected author: {selected_author}.")
    print(f"Selected theme: {selected_theme}.")


    

# rewrite input using selected author's style
    response = generate_response(user_input)
                    
    text_box.delete("1.0", "end")
    text_box.insert("1.0", response)


# record user input
def save_input():
    global user_input
    user_input = text_box.get("1.0", "end")

# window setting
window = tk.Tk()
window.title("Story Squire")
window.geometry("600x600")


# Create drop down menu for authors
author_options = ["None", "Edgar Allan Poe", "Hidetaka Miyazaki", "Stephen King", "H.P. Lovecraft", "George R. R. Martin", "J. R. R. Tolkien"]
author_var = tk.StringVar()
author_var.set("None")
author_dropdown = tk.OptionMenu(window, author_var, *author_options)
author_dropdown.pack()

# create drop down menu for themes
theme_options = ["None", "Fantasy", "Science Fiction", "Cthulhu Mythos", "Dark Fantasy", "Bleak", "Coming of age", "Dreams and reality", "The Supernatural"]
theme_var = tk.StringVar()
theme_var.set("None")
theme_dropdown = tk.OptionMenu(window, theme_var, *theme_options)
theme_dropdown.pack()

# Create text box where user write their story
text_box = tk.Text(window, width=60, height=20, font="Time 12")
text_box.pack()

# Create button
button = tk.Button(window, text="Save", command=save_input)
button.pack()

# Create an update button
update_button = tk.Button(window, text="Update", command=update_dropdown)
update_button.pack()

# Create a label to display the selected option
label = tk.Label(window, text="")
label.pack()

window.mainloop()

print(f"User input: {user_input}")
# print(f"User author: {chosen_option}")

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