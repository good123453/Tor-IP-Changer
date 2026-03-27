# -*- coding: utf-8 -*-

import time
import os
import subprocess
from pyfiglet import Figlet
from termcolor import colored

# Tool requirment system error handler included: if request module not download. Then handler run
try:

    import requests


# Handler system block : Download requests and requests[socks]
except Exception:

    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
    import requests


# Tor Finder system block : find your tor service -> if not finding tor then run handler
try:

    subprocess.run(["which", "tor"], check=True, capture_output=True, text=True)


# Handler system block: Download and install Tor and Update your repos
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')

    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install tor -y', shell=True)
    print('[!] tor is installed succesfully ')


# os command system : clear the terminal
os.system("clear")


# Internet Protocol checker system block
def get_ip_address() -> str | None:
    # request the url
    url = 'http://checkip.amazonaws.com'

    try:
        ip_response = requests.get(url, proxies=dict(    
            http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'), timeout=5)
        ip_response.raise_for_status()
        # recivive your ip address
        return ip_response.text.strip()

    except requests.exceptions.RequestException:
        print("NetworkError: your connection are weak")
        return None


# Internet Protocol Changer System block
def change_ip() -> None:
    try:
        subprocess.run(
            ["service", "tor", "reload"],
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print("Tor reload failed!")
        print(e.stderr)
        return

    Ip = get_ip_address()
    if Ip is not None:
        print(f"[+] Your IP has been Changed to: {Ip}")
        
    else:
        print("[+] Your IP has not been Changed: IP not found")


# logo system
def Banner(text="enter the text",fonts="ne",color="white"):
    
    coloroption = {"y": "light_yellow",
                    "b": "light_blue",
                    "c": "light_cyan",
                    "g": "light_green",
                    "m": "light_magenta",
                    "r": "light_red"}
    
    fonts_mapping = {"ne": "big_money-ne",
                     "nw": "big_money-nw",
                     "se": "big_money-se",
                     "sw": "big_money-sw"}
    
    f = Figlet(font=fonts_mapping.get(fonts, "big_money-ne"))
    
    colors = coloroption.get(color, "white")
    font_text = f.renderText(text)
    print(colored(font_text, colors))
    
Banner("Ip changer", "r")


# start tor system
try:
    subprocess.run(
                ["service", "tor", "start"],
                check=True,
                capture_output=True,
                text=True
            )
    
except subprocess.CalledProcessError as e:
    print("Tor start failed!")
    print(e.stderr)
    raise SystemExit(1)

time.sleep(3)

print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")


while True:

    try:
        change_interval_seconds = int(
            input("[+] time to change Ip in Sec [type=60] >> "))

        if change_interval_seconds <= 0:
            print("Time must be greater than 0")
            continue

        change_count = input(
            "[+] How many times do you want to change your IP? enter to infinite IP change] >> ").strip()

        if change_count != "":
            change_count = int(change_count)
            if change_count <= 0:
                print("Count must be greater than 0, or press Enter for infinite")
                continue

    except ValueError:
        print("Wrong Value! please enter the number!")
        continue

    else:

        break


# main logic

    # INFINITE IP CHANGE SYSTEM

if change_count == "":

    print("Starting infinite IP change. Press Ctrl+C to stop.")

    # infinite Ip change System
    while True:

        try:

            
            time.sleep(change_interval_seconds)

            change_ip()  

        except KeyboardInterrupt:

            print('\nAuto IP changer is closed.')

            break

else:

    # Ip address change by user times
    try:
        for Ipchange in range(change_count):

            
            time.sleep(change_interval_seconds)

            change_ip()  
            
    except KeyboardInterrupt:
        print("Ip Changer Tool is closed!")
