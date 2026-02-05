import os
import requests
import webbrowser
import sys
from rich import print
import time


def getreq():
    os.system('pip install colorama')
    os.system('pip install rich')
    os.system('clear')

def questify():
    url = "https://raw.githubusercontent.com/orqz/questify/refs/heads/main/games.json"
    data = requests.get(url).json()
    while True:
        gameselected = input("please selecte ur game : ").strip().lower()
        gamedata = data.get(gameselected)
        if gamedata == None:
            os.system('cls')
            print(f"{gameselected} does not exist")
        else:
            game_exe = gamedata['exe']
            game_folder = gamedata['folder']
            currentfile = os.path.abspath(sys.argv[0])
            os.mkdir(game_folder)
            os.rename(currentfile, os.path.join(game_folder, game_exe))
            timer()

   
def showlist():
    webbrowser.open_new_tab('https://github.com/orqz/questify/blob/main/games.json')

def die():
    os.system('exit')
    
def timer():
    time.sleep(15)    



banner = r"""
                              __           ___             
                             /\ \__  __  /'___\            
   __   __  __     __    ____\ \ ,_\/\_\/\ \__/  __  __    
 /'__`\/\ \/\ \  /'__`\ /',__\\ \ \/\/\ \ \ ,__\/\ \/\ \   
/\ \L\ \ \ \_\ \/\  __//\__, `\\ \ \_\ \ \ \ \_/\ \ \_\ \  
\ \___, \ \____/\ \____\/\____/ \ \__\\ \_\ \_\  \/`____ \ 
 \/___/\ \/___/  \/____/\/___/   \/__/ \/_/\/_/   `/___/> \
      \ \_\                                          /\___/
       \/_/                                          \/__/ 

                     >> github.com/orqz <<
"""

def rename():
    currentfile = os.path.abspath(sys.argv[0])
    os.rename(currentfile, 'questify.exe')
    os.system("cls")

def menu():
    print(banner)
    print(" [1] Start Questify :) ")
    print(" [2] Game List ")
    print(" [3] Exit ")

    i = input()
    
    match i:
        case "1":
            questify()
        case "2":
            showlist()
            os.system("cls")
            menu()
        case "3":
            die()


#if not "questify.exe" in os.path.abspath(sys.argv[0]):
    #rename()


menu()




