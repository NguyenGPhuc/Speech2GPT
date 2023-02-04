# create a log of the conversation
def write_log(text, log):
    # keep a temporary file for easy access and editing current passage
    f_temp = open("temp.txt", 'w')
    f_temp.write(text)
    f_temp.close()

    # add tempory passage into the story.
    if log == 1:
        with open("temp.txt", 'r') as firstFile, open('record.txt', 'a') as secondFile:
            for line in firstFile:
                secondFile.write(line)

# read from record file
def read_log(which_log):
    if which_log == 1:
        f = open("record.txt", 'r')
        return f.read()
    else:
        # read from temporary log
        f_temp = open("temp.txt", 'r')
        return f_temp.read()