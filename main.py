import os
import sys
import shutil
import time
import requests
import webbrowser



def quest():

    try:
        import requests
    except ImportError:
        os.system('pip install requests')

    os.system('cls')
    
    while True:
        url = "https://raw.githubusercontent.com/orqz/questify/refs/heads/main/games.json"
        data = requests.get(url).json()
        gameselected = input("please selecte ur game : ").strip().lower()
        gamedata = data.get(gameselected)
        if gamedata == None:
            os.system('cls')
            print(f"{gameselected} does not exist")
        else:
            game_exe = gamedata['exe']
            game_folder = gamedata['folder']
            src = "questify.exe"
            dst = os.path.join(game_folder, "questify.exe")
            os.mkdir(game_folder)
            shutil.copy(src, dst)
            new_name = os.path.join(game_folder, game_exe + ".exe")
            os.rename(dst, new_name)
            print(f"{game_folder} Folder has been Created :) open the {game_exe}.exe inside it and enjoy")
            time.sleep(15)

def timer():
    total_seconds = 15 * 60 + 30  

    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        print(f"\rTime left: {minutes:02d}:{seconds:02d}", end="", flush=True)
        time.sleep(1)
        total_seconds -= 1

    print("\rTime left: 00:00")
    sys.exit(0) 

def showlist():
    webbrowser.open_new_tab('https://github.com/orqz/questify/blob/main/games.json')
    
def die():
   sys.exit(0) 
    
def menu():
    print(banner)
    print(" [1] Start Questify : ") 
    print(" [2] Game List ")
    print(" [3] Exit ")

    i = input()
    
    match i:
        case "1":
            quest()
        case "2":
            showlist()
        case "3":
            die()
        



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


if os.path.exists('questify.exe'):
    menu()
else:
    timer()
