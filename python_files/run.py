
import main

import color
import importlib
import os
import logger
import requests
import sys
from colorama import just_fix_windows_console, Fore, Style, Back






#COLORES  
red  = Fore.RED + Style.BRIGHT
purp = Fore.MAGENTA  + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
yell = Fore.YELLOW + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
back_yell = Fore.BLACK + Style.BRIGHT + Back.YELLOW
green= Fore.GREEN + Style.BRIGHT
#---------------------------------------------------





def reset_mod(mod_name):
    if mod_name in sys.modules:
    	importlib.reload(sys.modules[mod_name])


main.control()






