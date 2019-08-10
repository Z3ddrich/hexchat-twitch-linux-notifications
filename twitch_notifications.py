__module_name__ = "Twitch_Notifications"
__module_version__ = "1.0"
__module_author__ = "Mysterious_Loner"
__module_description__ = "Display messages as system notifications"

import hexchat
import os
import sys

# Display message as system notification

def twitch_notify(word, word_eol, userdata):
    
    nick = word[0]
    message = ' '.join(word[3:])
    start ='!'
    end = '@'
    os.system('notify-send -t 120000 "' +nick.split(start)[1].split(end)[0].upper() +' ' +message +'"')
    return hexchat.EAT_NONE

# Capture every message for twitch_notify()

hexchat.hook_server("PRIVMSG", twitch_notify)
