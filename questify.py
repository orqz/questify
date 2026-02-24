import os
import sys
import shutil
import time
import requests
import webbrowser
import difflib


url = "https://discord.com/api/applications/detectable"
gamelist = requests.get(url).json()


def menu():
    print(banner)
    print(" [1] Start Questify")
    print(" [2] Discord Server")
    print(" [3] Exit")

    choice = input("> ")

    if choice == "1":
        start_questify()
    elif choice == "2":
        webbrowser.open_new_tab("https://discord.gg/vRFXc3pvt4")
    elif choice == "3":
        sys.exit(0)


def start_questify():
    names = []

    for app in gamelist:
        if app["name"]:
            names.append(app["name"])

    gselect = input("Select game: ").strip().lower()

    matches = difflib.get_close_matches(gselect, names, n=10, cutoff=0.4)

    if len(matches) == 0:
        print("No matches.")
        return

    i = 1
    for name in matches:
        print(f"[{i}] --> {name}")
        i = i + 1

    sel = int(input("Select number: "))
    selected_name = matches[sel - 1]

    print("Selected:", selected_name)

    exename = None

    for app in gamelist:
        if app["name"] == selected_name:
            for exe in app["executables"]:
                if exe["os"] == "win32" and exe["is_launcher"] == False:
                    exename = exe["name"]
                    break

    if exename is None:
        print("No Windows executable found.")
        return

    src = "questify.exe"

    parts = exename.split("/")

    if len(parts) > 1:
        folder = selected_name
        index = 0

        while index < len(parts) - 1:
            folder = os.path.join(folder, parts[index])
            index = index + 1

        exe_file = parts[-1]
    else:
        folder = selected_name
        exe_file = exename

    os.makedirs(folder, exist_ok=True)

    dst = os.path.join(folder, exe_file)
    shutil.copy(src, dst)

    print("\nInstalled:")
    print(dst)
    print("Run this exe to launch Questify.")

    time.sleep(10)


def timer():
    total = 15 * 60 + 30

    while total > 0:
        m = total // 60
        s = total % 60
        print(f"\rTime left: {m:02d}:{s:02d}", end="", flush=True)
        time.sleep(1)
        total = total - 1

    print("\rTime left: 00:00")
    sys.exit(0)


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


if os.path.exists("questify.exe"):
    menu()
else:
    timer()
