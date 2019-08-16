__module_name__ = "Twitch_Notifications"
__module_version__ = "2.0"
__module_author__ = "Mysterious_Loner"
__module_description__ = "Display messages and streamevents as system notifications"

import hexchat
import os
import sys

# Display message as system notifications
def twitch_notify(word, word_eol, userdata):
    
    nick = word[0].split('!')[1].split('@')[0].upper()
    message = ' '.join(word[3:])
    os.system('notify-send -t 120000 "' +nick +' ' +message +'"')
    return hexchat.EAT_NONE

# Display streamalerts as system nofications
def streamalerts(word, word_eol, userdata):

    capture = ' '.join(word[0:])
    for line in capture:
        print(capture + '\n')
    return hexchat.EAT_NONE

hexchat.hook_server("PRIVMSG", twitch_notify)
hexchat.hook_server("USERNOTICE", streamalerts)

