# create a log of the conversation
def write_log(temp):
    # keep a temporary file for easy access and editing current passage
    f_temp = open("output/temp.txt", 'w')
    f_temp.write(temp)
    f_temp.close()

# read from record file
def read_log(which_log):
    if which_log == 1:
        f = open("record.txt", 'r')
        return f.read()
    else:
        # read from temporary log
        f_temp = open("temp.txt", 'r')
        return f_temp.read()