# import speech_recognition as sr
# import openai
import os
from text2speech import *
from openai_service import *
from speech2text import *
from writing_log import *
from command_option import *

# program will continuously ask user for a prompt
while True:
        # reading from speech-to-text
        # text_speech = speech_to_text()
        # text = speech_to_text()

        # reading from user keyboard input
        # text_input = input('Write or say a promt\n')
        ask = input('Write or say a promt\n')
        text = ''

        # write_log(text, log)

        # program will close upon hearing "close chat" or "end chat"
        if ask == 'close chat' or ask == 'end chat':
            break

        else:
            # checks to see if speech was successfully converted to text
            if ask != "Sorry, I did not get that":        
                # if user want to ask openAI to do something instead of writing.
                if (ask == 'ask ai' or ask == 'ask chat'):
                    text = input('Ask promt or tpye a command: ')
                    voice_option = check_voice(text, voice_option)
                    log_status = check_log(text, log_status)

                    # program will close upon hearing "close chat" or "end chat"
                    if text == 'close chat' or text == 'end chat':
                        break

                    response = generate_response(text)
                    print(f"Response: {response}\n")
                    # only temperory log will be kept and will be deleted after each response.
                    # permanent log will be recorded if option is enabled.
                    write_log(response, log_status)

                # if user want to check current sentence or paragrph's grammar
                elif (text == 'check grammar' or text == 'check pargraph'):
                    voice_option = check_voice(text, voice_option)
                    log_status = check_log(text, log_status)

                    read_log()

                # simply record speech to text log.
                else:

                    voice_option = check_voice(text, voice_option)
                    log_status = check_log(text, log_status)

                    # write_log(speech_to_text(), log_status)
                    write_log(text, log_status)
            else:
                print(text) 

                # print(f"Response: {response}\n")


            # text to speech will read the response if enabled
            if (voice_option == 1):
                speech_response(response)