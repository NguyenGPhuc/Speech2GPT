
from text2speech import speech_response

#default voice option off
voice_option = 0

# default log option is on
log_status = 1

# functional that voice option
def check_voice(text, voice_option):
    # enable voiced option while program is running by saying "voice option ON"
    if text == 'voice option on':
        if voice_option != 1:
            voice_on = "Voice option is now on"
            print(voice_on)
            speech_response(voice_on)
            voice_option = 1
    # disable voiced option while program is running by saying "voice option OFF"
    else:
        if voice_option != 0:
            print("Voice option is now off")
            # speech_response(voice_off)
            voice_option = 0

    return voice_option

# function that handle log option
def check_log(text, log):
    # enable permanent log option
    if text == 'log option on':
        if log != 1:
            log = 1
    # disable log option
    else:
        if log != 0:
            log = 0

    return log

# funtion that handle all user commands
def command_line(text):
    # command for closing chat.
    if text == 'close chat' or text == 'end chat':
        command = 'terminate'
        return command
    
    # command for asking ai option
    elif text == 'ask ai' or text == 'ask chat':
        command = 'ask ai'
        return 'ask ai'
    # command for closing ai option
    elif text == 'close ai' or text == 'quit ai':
        command = 'close ai'
        return command
    
    # command to open writing mode
    elif text == 'writing mode' or text == 'write mode':
        command = 'writing mode'
        return command

    else:
        command = "Sorry, I did not get that"