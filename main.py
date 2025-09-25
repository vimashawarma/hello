
# literally packages to download:
#import sys, platform ,os,pyautogui,keyboard, time
#from colorama import Fore, init


version = "1.0.0"
credits = "keke"

# custom settings or configs whatever its fucking called:

loop_delay = 1     # dis is how many seconds it waits before starting a new loop
click_delay = 0.1  # dis is how many seconds it waits before clicking the mouse between each button, for exmple it clicks send To, waits 'x' seconds, then clicks your shortcut, etc


position_delay = 0.5 # recommend do not touch this. Does not affect the speed of the bot itself.


"""
disclaimer:

yo keke here — i made this snap script. use it at your own risk.
i not responsible if stuff goes sideways or you get locked out.
this thing has zero affiliation with snapchat (no sponsorship, no support, nada).
automating your account might break Snapchat’s TOS and get your account banned or disabled.
this is for learning/education only. don’t be dumb.

"""

a_text = rf"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣷⢸⣿⣿⡜⢯⣷⡌⡻⣿⣿⣿⣆⢈⠻⠿⢿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⢳⣿⣿⣿⣿⣿⣿⡜⣿⣿⣧⢀⢻⣷⠰⠈⢿⣿⣿⣧⢣⠉⠑⠪⢙⠿⠿⠿⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣱⡇⡞⣿⣿⣿⣿⣿⣿⡇⣿⣿⡏⡄⣧⠹⡇⠧⠈⢻⣿⣿⡇⢧⢢⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⢃⢿⣿⣿⣿⣿⣿⣷⣿⣿⠇⢃⣡⣤⡹⠐⣿⣀⢻⣿⣿⢸⡎⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣾⣿⣿⠘⡸⣿⣿⣿⣿⣿⣿⣿⡿⣰⣿⣿⢟⡷⠈⠋⠃⠎⢿⣿⡏⣿⠀⠘⢆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⢹⣿⣿⡐⢡⢹⣿⣿⣿⣿⡏⣿⢣⣿⣿⡑⠁⠔⠀⠉⠉⠢⡘⣿⡇⣿⡇⠀⡀⠡⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠘⣿⣿⣇⠇⢣⢻⣿⣿⣿⡇⢇⣾⣿⣿⡆⢸⣤⡀⠚⢂⠀⢡⢿⡇⣿⡇⠀⢿⠀⠀⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠠⠹⣿⣿⡘⣆⢣⠻⣿⣿⢈⣾⣿⣿⣿⣶⣸⣏⢀⣬⣋⡼⣠⢸⢹⣿⡇⢠⣼⠙⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠁⠹⣿⣇⠹⡃⠃⠙⡇⠘⢿⣿⣿⣿⣿⣿⣏⣓⣉⣭⣴⣿⠘⢸⣿⠁⠘⠋⠀⠹⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠈⢿⣇⠂⣷⠄⠐⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⢸⡏⠀⢀⣠⣴⣾⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠙⠆⠈⠢⠲⠥⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡞⣸⠁⠀⢸⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠃⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡏⠹⣿⣿⡿⠫⠊⠀⠀⠀⣶⠀⢻⣿⣿⣿⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠿⠿⠿⢋⠀⠀⠀⠀⢀⣼⣿⡆⠈⣿⣿⣿⡟⣱⡷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⣁⡀⠨⣛⠿⠶⠄⢀⣠⣾⣿⣿⣷⠀⢹⣿⡟⣴⠈⢃⣶⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⣿⣿⡿⠀⡀⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⠻⣿⣿⢀⠙⠻⠿⣿⣿⣿⣿⣿⣿⡇⠁⣿⠟⡀⠈⣧⢰⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠴⠮⣥⠻⢧⣤⣄⣀⡉⢩⣭⣍⣃⣀⣩⠎⢀⣼⠉⣼⡯⠀⠀{credits}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠁⣛⠓⢒⣒⣢⡭⢁⡈⠿⠿⠟⠹⠛⠁⠀⠀⠀⠰⠃⠂⠀⠀⠀v1.0.0"""


required_modules = {
    'colorama': 'from colorama import Fore, init, Style',
    'ctypes': 'import ctypes',
    'pyautogui': 'import pyautogui',
    'keyboard': 'import keyboard',
    'os': 'import os',
    'time': 'import time',
    'platform': 'import platform',
    'datetime': 'from datetime import datetime',
    'sys': 'import sys',
    'requests': 'import requests',

}
missing_modules = []

for module, statement in required_modules.items():
    try:
        exec(statement, globals())
    except ImportError:
        missing_modules.append(module)

if missing_modules:
    print("error. unable to import one or more required modules")
    print("please make sure you open the 'Install_Requirements.bat' file before using this program.")
    print("\nfor the python pros, you are missing the following modules:")
    for mod in missing_modules:
        print(f" - {mod}")
    input()
    sys.exit(1)


init(autoreset=True, convert=True)

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def title(x):
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(x)
    else:
        # for Linux/macOS terminals supporting ANSI escape codes:
        sys.stdout.write(f"\33]0;{x}\a")
        sys.stdout.flush()

def nice_print(x, status = "-"):
    print(f"{Fore.WHITE}[{Fore.CYAN}{status}{Fore.WHITE}] {x}")

class snap_bot:

    def __init__(self):
        self.sent_snaps = 0
        self.first_try = True

    def get_positions(self):
        nice_print("move your mouse to the camera button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.switch_to_camera = pyautogui.position()
                break
        time.sleep(position_delay)
        nice_print("move your mouse to the send to button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.send_to = pyautogui.position()
                break
        time.sleep(position_delay)
        nice_print("move your mouse to your shortcut button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.shortcut = pyautogui.position()
                break
        time.sleep(position_delay)
        nice_print("move your mouse to the select all in shortcut button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.select_all = pyautogui.position()
                break
        time.sleep(position_delay)

    def send_snap(self, started_time, shortcut_user_count):
        self.update_title(started_time, shortcut_user_count)
        pyautogui.moveTo(self.switch_to_camera)
        if self.first_try:
            pyautogui.click() # activates the snap feature, only need to do this once.
            self.first_try = False
        time.sleep(click_delay)
        pyautogui.click() # takes the snap.
        time.sleep(click_delay)
        pyautogui.moveTo(self.send_to)
        pyautogui.click()
        time.sleep(click_delay)
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(click_delay)
        pyautogui.moveTo(self.select_all)
        pyautogui.click()
        time.sleep(click_delay)
        pyautogui.moveTo(self.send_to) # same position.
        pyautogui.click()
        self.sent_snaps += 1
        self.update_title(started_time, shortcut_user_count)
    
    def update_title(self, started_time, shortcut_user_count):

        now = time.time()
        elapsed = str(now - started_time).split(".")[0]
        new_snaps = self.sent_snaps * shortcut_user_count
        title(f"snoopdawg booster | sent: {new_snaps} | Elapsed: {elapsed}s | {credits}")

        clear()
        print(Fore.CYAN + a_text)
        nice_print("snaps sent", new_snaps)

def main():
    clear()
    title(f"snoopdawg booster | {credits}")
    print(Fore.CYAN + a_text)
    nice_print("Start", "1")
    nice_print("Help and Instructions", "2")
    nice_print("Disclaimer", "3")
    try:
        option = int(input(f"\n{Fore.CYAN}> {Fore.WHITE}"))
    except ValueError:
        return main()
    if option == 1:
        try:
            shortcut_user_count = int(input(f"\n{Fore.WHITE}[{Fore.CYAN}-{Fore.WHITE}] How many people are in your shortcut: "))
        except ValueError:
            return main()
        
        
        obj = snap_bot()
        print()
        obj.get_positions()
        print()
        nice_print("positions are saved. go back to the beginning, press F when you are ready.")
        while True:
            if keyboard.is_pressed("f"):
                break
        clear()
        print(Fore.RED + a_text)
        nice_print("sending snaps...")
        started_time = time.time()
        while True:
            obj.send_snap(started_time, shortcut_user_count)
            time.sleep(loop_delay)
    elif option == 2:
        print()
        nice_print("this program only works with snapchat web.", "-")
        print()
        nice_print("instructions:", "-")
        nice_print("on your phone, open snapchat, create a shortcut with as many people as possible to spam snaps to", "1")
        nice_print("download snapchat web on a computer", "2")
        nice_print("login and allow permissions to your camera/microphone/etc", "3")
        nice_print("if you don't have a camera, download OBS Studio and get a virtual camera.", "4")
        nice_print("you may need to restart your pc if you only downloaded a virtual camera just now.", "5")
        nice_print("open this program and select the start option and begin.", "6")
        nice_print("press 'enter' to go back to the main menu.", "-")
        input()
        return main()
    elif option == 3:
        print()
        nice_print("disclaimer:", "!")
        nice_print("use it at your own risk.", "-")
        nice_print("i not responsible if stuff goes sideways or you get locked out.", "-")
        nice_print("this thing has zero affiliation with snapchat (no sponsorship, no support, nada).", "-")
        nice_print("automating your account might break Snapchat’s TOS and get your account banned or disabled.", "-")
        nice_print("this is for learning/education only. don’t be autistic.", "-")
        nice_print("press 'enter' to go back to the main menu.", "-")
        input()
        return main()
    else:
        return main()


        


if __name__ == "__main__":
    main()

