import tkinter as tk
import re
from openai_service import *
from speech2text import *
from writing_log import *
from command_option import *
from tkinter import Label
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

chosen_theme = ''
chosen_theme = ''

# keep track of current page and paragraph
paragraph_num = 1
page_num = 1
book_num = 1

# keep track of current passage and saved passage
user_input = ''
saved_input = ''

# create output directory
output_diectory = "output"
file_name = ''
current_path = os.path

# generate passage using current passage.
def generate_passage():
# drop down menu for authors
    global chosen_author
    selected_author = author_var.get()
    if selected_author == "None":
        chosen_author = "None"
    else:
        chosen_author = selected_author

    # drop down menu for authors theme
    global chosen_theme
    selected_theme = theme_var.get()
    if selected_theme == "None":
        chosen_theme = "None"
    else:
        chosen_theme =  selected_theme

    # use current passage as prompt
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

    print(f"Selected author: {selected_author}.")
    print(f"Selected theme: {selected_theme}.")

    # Allow AI to either modify passage or checks its grammar
    response = generate_response(selected_author, selected_theme, user_input)
                    
    text_box.delete("1.0", "end")
    text_box.insert("1.0", response.strip())


# save the current passage
def save_input():
    global saved_input
    saved_input = text_box.get("1.0", "end").strip()

# save current pasage to file
def save_page():
    # save current passage to a file as 1 paragraph.
    global user_input
    if user_input == 'No passage was previously saved':
        user_input = ''
    raw_input = text_box.get("1.0", "end")
    user_input = raw_input.strip()

    global paragraph_num
    global page_num
    global file_name

    # create an output directory of 
    global output_diectory
    if not os.path.exists(output_diectory):
        os.makedirs(output_diectory)
    

    # each page should only contains 5 paragraph before a new page is created.
    if paragraph_num <= 5:
        file_name = "page (" + str(page_num) + ")"
        file_path = os.path.join(output_diectory, file_name)
        with open(file_path, "a") as file:
            file.write("Paragraph (" + str(paragraph_num) + ")" + "\n" + user_input + "\n\n")
            paragraph_num += 1

    # new page will be created when 5 paragraph limit is reach.
    else:
        paragraph_num = 1
        page_num += 1
        file_name = "page (" + str(page_num) + ")"
        file_path = os.path.join(output_diectory, file_name)
        with open(file_path, "a") as file:
            file.write("Paragraph (" + str(paragraph_num) + ")" + "\n" + user_input + "\n\n")
            paragraph_num += 1
        

# load saved passage
def load_input():
    global saved_input
    if saved_input == '':
        saved_input = "No passage was previously saved"

    text_box.delete("1.0", "end")
    text_box.insert("1.0", saved_input)

# load passage with user given paragraph and page number
def load_page():
    global paragraph_num
    global page_num
    global file_name

    load_window = tk.Toplevel(window)
    load_window.title("Load Window")

    label1 = tk.Label(load_window, text="Enter page number:")
    label1.grid(row=0, column=0)
    entry1 = tk.Entry(load_window)
    entry1.grid(row=0, column=1)

    label2 = tk.Label(load_window, text="Enter paragraph number:")
    label2.grid(row=1, column=0)
    entry2 = tk.Entry(load_window)
    entry2.grid(row=1, column=1)

    # create an output directory of 
    global output_diectory
    if not os.path.exists(output_diectory):
        print("No saved files")


# window setting
window = tk.Tk()
window.title("Story Squire")
window.geometry("900x800")

# frame for description
frame1 = tk.Frame(window)
frame1.pack()

# describe dropdown menu for author
author_label = tk.Label(frame1, text="Select Author Style")
author_label.pack(side="left", padx=10)

# describe dropdown menu for theme
theme_label = tk.Label(frame1, text="Select a theme")
theme_label.pack(side="left", padx=10)

# frame dropdown menu is in
frame2 = tk.Frame(window)
frame2.pack(pady=20)

# Create drop down menu for authors
author_options = ["None", "Edgar Allan Poe", "Hidetaka Miyazaki", "Stephen King", "H.P. Lovecraft", "George R. R. Martin", "J. R. R. Tolkien"]
author_var = tk.StringVar()
author_var.set("None")
author_dropdown = tk.OptionMenu(frame2, author_var, *author_options)
author_dropdown.pack(side="left", padx=20)

# create drop down menu for themes
theme_options = ["None", "High Fantasy", "Science Fiction", "Cthulhu Mythos", "Dark Fantasy", "Romance", "Bleak", "Coming of age", "Dreams and reality", "The Supernatural", "Comedy"]
theme_var = tk.StringVar()
theme_var.set("None")
theme_dropdown = tk.OptionMenu(frame2, theme_var, *theme_options)
theme_dropdown.pack(side="left", padx=20)

# frame user input is in
frame3 = tk.Frame(window)
frame3.pack(pady=20)

# Create text box where user write their story
text_box = tk.Text(frame3, width=80, height=20, font="Time 12")
text_box.pack(side="left")

# from for save and load current passage
frame4 = tk.Frame(window)
frame4.pack(pady=20)

# Create save button
save_button = tk.Button(frame4, text="Save", command=save_input)
save_button.pack(side="left")

# create load button
load_button = tk.Button(frame4, text="Load", command=load_input)
load_button.pack(side="left")

frame5 = tk.Frame(window)
frame5.pack(pady=20)

# create a save to file button
save_to_page = tk.Button(frame5, text="Save to page", command=save_page)
save_to_page.pack(side="left")

# create a load from file button
load_from_page = tk.Button(frame5, text="Load from page", command=load_page)
load_from_page.pack(side="left")

# Create an update button
update_button = tk.Button(window, text="Generate", command=generate_passage)
update_button.pack()

# Create a label to display the selected option
label = tk.Label(window, text="")
label.pack()


window.mainloop()