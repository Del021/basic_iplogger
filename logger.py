
#ip logger by: Del0

# ---------------------
import importlib
import sys
import os
import re
import requests
import textwrap
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
#----------------------

#Data
with open('url.dat', 'r') as archivo:
    archivo.flush()
    url = archivo.read()

#---------------------------------


#COLORES  
red  = Fore.RED + Style.BRIGHT
purp = Fore.MAGENTA  + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
yell = Fore.YELLOW + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
back_yell = Fore.BLACK + Style.BRIGHT + Back.YELLOW
green= Fore.GREEN + Style.BRIGHT
#---------------------------------------------------


#URL del ip logger
website = url

#-------------
resultado = 0
content = 0

if website != '':
    resultado = requests.get(website)
    content = resultado.text
else:
    pass
try: 
    soup = BeautifulSoup(content, 'html.parser')

# Buscar las etiquetas <div> con la clase "ip-address" y extraer las direcciones IP
# Filtra la etiqueta para dar las direcciones ip
    ip_tags = soup.find_all('div', class_='ip-address')
    ip_addresses = [tag.get_text() for tag in ip_tags]


# Filtra los dispositivos conectados y sus versiones
    so_Ver_tags = soup.find_all('div', class_='visitor-useragent')
except TypeError:
    pass
try:
    user_Version= [tag.get_text() for tag in so_Ver_tags]
    user_Version.remove('Identificador de dispositivos')
except:
    pass
 

def salida():
    cont = 0
    print(f'{back_yell}INTERPRETACIÓN:{Style.RESET_ALL}\n {yell}Dirección ip \n{green}Software y versiones')
    print('\n')
    for i in ip_addresses:
        print(f'{yell}{i}:     \n{green}{user_Version[cont]}\n' )
        cont = cont +1


