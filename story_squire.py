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

user_input = ''
saved_input = ''

# drop down menu for authors
def update_dropdown():
    global chosen_author
    selected_author = author_var.get()
    if selected_author == "None":
        chosen_author = "None"
    else:
        chosen_author = selected_author

    global chosen_theme
    selected_theme = theme_var.get()
    if selected_theme == "None":
        chosen_theme = "None"
    else:
        chosen_theme =  selected_theme

    global user_input
    if user_input == 'No passage was previously saved':
        user_input = ''
    raw_input = text_box.get("1.0", "end")
    user_input = raw_input.strip()

    # keep user up-to-date with what's happening after "Generate" button is press.
    if user_input == '' and chosen_author != 'None' and chosen_theme != 'None':
        label.config(text="AI have generated a story using author [ " + chosen_author + " ] style with a [ " + chosen_theme + " ] theme.")
    elif user_input  == '' and chosen_author != 'None' and chosen_theme == 'None':
        label.config(text="AI have generated a story using author [ " + chosen_author + " ] style with no specific theme.")
    elif user_input == '' and chosen_author == 'None' and chosen_theme != 'None':
        label.config(text="AI have generated a story with a ["  + chosen_theme + "] theme.")
    elif user_input  == '' and chosen_author == 'None' and chosen_theme == 'None':
        label.config(text="AI have generated a random story")
    else:
        label.config(text="Your passage was modify to match author [ " + chosen_author + " ] style with a [ " + chosen_theme + " ] theme.")
    print(f"Selected author: {selected_author}.")
    print(f"Selected theme: {selected_theme}.")
    print(user_input)


    # Allow AI to either modify passage or checks its grammar
    response = generate_response(selected_author, selected_theme, user_input)
                    
    text_box.delete("1.0", "end")
    text_box.insert("1.0", response.strip())

# save the current passage
def save_input():
    global saved_input
    saved_input = text_box.get("1.0", "end").strip()

# save current pasage to file
def save_to_page():
    global user_input
    word_count = 0
    paragraph_count = 1
    page_count = 1

    file = open(os.path.joint("/output", "page_"+page_count, "x")) 


    with open (os.path.joint("/output", "page_"+1, "w")) as file:
        file.write(user_input)

# load saved passage
def load_input():
    global saved_input
    if saved_input == '':
        saved_input = "No passage was previously saved"

    text_box.delete("1.0", "end")
    text_box.insert("1.0", saved_input)

# window setting
window = tk.Tk()
window.title("Story Squire")
window.geometry("900x800")

# Create drop down menu for authors
author_options = ["None", "Edgar Allan Poe", "Hidetaka Miyazaki", "Stephen King", "H.P. Lovecraft", "George R. R. Martin", "J. R. R. Tolkien"]
author_var = tk.StringVar()
author_var.set("None")
author_dropdown = tk.OptionMenu(window, author_var, *author_options)
author_label = tk.Label(window, text="Select Author Style")
author_dropdown.pack()
author_label.pack()

# create drop down menu for themes
theme_options = ["None", "High Fantasy", "Science Fiction", "Cthulhu Mythos", "Dark Fantasy", "Romance", "Bleak", "Coming of age", "Dreams and reality", "The Supernatural", "Comedy"]
theme_var = tk.StringVar()
theme_var.set("None")
theme_dropdown = tk.OptionMenu(window, theme_var, *theme_options)
theme_label = tk.Label(window, text="Select a theme")
theme_dropdown.pack()
theme_label.pack()

# Create text box where user write their story
text_box = tk.Text(window, width=80, height=20, font="Time 12")
text_box.pack()

frame = tk.Frame(window)
frame.pack(pady=10)


# Create save button
save_button = tk.Button(window, text="Save", command=save_input)
save_button.pack()

# create load button
load_button = tk.Button(window, text="Load", command=load_input)
load_button.pack()

# Create an update button
update_button = tk.Button(window, text="Generate", command=update_dropdown)
update_button.pack()

# Create a label to display the selected option
label = tk.Label(window, text="")
label.pack()


window.mainloop()