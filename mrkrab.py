import random
import psutil
import getpass
import itertools
import platform
import datetime

def main():
    def main1():
        return random.randint(0, 3)

    def main2():
        return random.randint(0, 23)

    usr_name = getpass.getuser()
    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024 ** 3), 2)
    ram_used = round(ram.used / (1024 ** 3), 2)
    storage = psutil.disk_usage('/')
    storage_total = round(storage.total / (1024 ** 3), 2)
    storage_used = round(storage.used / (1024 ** 3), 2)
    os_name = platform.system()
    os_version = platform.release()
    kernel_version = platform.uname().release
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    x = "\033[38;2;250;128;114m"

    def main3():
        return random.randint(0, 2)

    def main4():
        return random.randint(0, 23)

    # Color definitions
    colors = {
        "Red": "\033[31m",
        "Green": "\033[32m",
        "Yellow": "\033[33m",
        "Blue": "\033[34m",
        "Magenta": "\033[35m",
        "Cyan": "\033[36m",
        "Bright_Red": "\033[91m",
        "Bright_Green": "\033[92m",
        "Bright_Yellow": "\033[93m",
        "Bright_Blue": "\033[94m",
        "Bright_Magenta": "\033[95m",
        "Bright_Cyan": "\033[96m",
        "Light_Red": "\033[38;2;255;100;100m",
        "Light_Green": "\033[38;2;100;255;100m",
        "Light_Blue": "\033[38;2;100;100;255m",
        "Light_Yellow": "\033[38;2;255;255;100m",
        "Light_Cyan": "\033[38;2;100;255;255m",
        "Light_Magenta": "\033[38;2;255;100;255m",
        "Light_Gray": "\033[38;2;211;211;211m",
        "Olive": "\033[38;2;128;128;0m",
        "Teal": "\033[38;2;0;128;128m",
        "Navy": "\033[38;2;0;0;128m",
        "Pink": "\033[38;2;255;192;203m",
        "Gold": "\033[38;2;255;215;0m",
        "Salmon": "\033[38;2;250;128;114m",
        "Turquoise": "\033[38;2;64;224;208m"
    }

    color_names = list(colors.keys())
    y = colors[color_names[main4()]]

    num = main3()
    if num == 0:
        a = r" __  __                                 "
        b = r"|  \/  |    _ _                         "
        c = r"| |\/| |   | '_|                         "
        d = r"|_|__|_|  _|_|_                          "
        e = r'''_|"""""|_|"""""|                         '''
        f = r'''"`-0-0-'"`-0-0-'                         '''
        g = r"  _  __                   _              "
        h = r" | |/ /     _ _   __ _   | |__     ___   "
        i = r" | ' <     | '_| / _` |  | '_ \   (_-<   "
        j = r" |_|\_\   _|_|_  \__,_|  |_.__/   /__/_  "
        k = r'''_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| '''
        l = r'''"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' '''
        m = ""
    elif num == 1:
        a = r"__  __                "
        b = r" |  \/  |_ _            "
        c = r" | |\/| | '_|           "
        d = r" |_| _|_|_|     _       "
        e = r" | |/ /_ _ __ _| |__ ___"
        f = r" | ' <| '_/ _` | '_ (_-<"
        g = r" |_|\_\_| \__,_|_.__/__/"
        h = i = j = k = l = m = ""
    else:
        a = r"  \\    ///()_()"                       
        b = r" ((O)  (O))(O o)   "                    
        c = r"  | \  / |  |^_\     "                  
        d = r"  ||\\//||  |(_))      "                
        e = r"  || \/ ||  |  /         "              
        f = r"  ||    ||  )|\\           "            
        g = r" (_/    \_)()_())        ___    oo_   " 
        h = r"  (OO) .' )(O o)    /)  (___)__/  _)-< "
        i = r"   ||_/ .'  |^_\  (o)(O)(O)(O) \__ `.  "
        j = r"   |   /    |(_))  //\\ /  _\     `. | "
        k = r"   ||\ \    |  /  |(__)|| |_))    _| | "
        l = r"  (/\)\ `.  )|\\  /,-. || |_)) ,-'   | "
        m = r"       `._)(/  \)-'   ''(.'-' (_..--'  "

    def img1():
        art = [
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀ ",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⠂⣠⠞⢿⠀⠀⠀⠀⠀  ",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠁⠘⢠⠃⢀⠏⠀⠀⠀⠀⠀⠀",
            r"                                               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡀⠇⣎⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⢀⠠⠤⠄⡀⠀⠀⠀⠀⠀⡟⢳⢸⠛⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⢀⠌⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠇⠘⢸⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⡈⠀⠀⠀⠀⡤⠉⣀⠀⠀⠀⠀⢠⠀⢸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⢁⠀⠀⠀⠰⡇⢰⠃⢰⠀⠀⠀⠈⣾⢸⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠈⢄⠀⠀⠀⠢⠋⢀⠎⠀⠐⢤⣄⣸⠛⠾⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠑⠂⢠⢰⠀⠁⠀⠀⠀⣠⠚⠩⢀⡠⠤⠀⢳⡀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠈⠄⠆⠀⠠⢦⡶⡷⣀⣀⠤⠤⡔⠂⠁⠠⣉⣯⠅⢒⢢⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⣔⢏⠀⠀⠋⠀⠑⠊⠀⠀⠀⠀⣘⣄⠀⣌⡮⠀⣀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⡴⣽⣖⡿⢶⣦⠤⠤⠤⠤⠤⠔⢒⡫⠕⢫⡾⠃⠀⣀⣀⡇⠀⠀",
            r"                                                 ⠀⠀⠀⠀⠀⠀⠠⠃⠉⠹⠷⣾⠇⠈⢉⣉⣉⡇⠸⠔⠊⠹⠀⠀⠛⣯⣁⠞⠀⢣",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠣⡀⠀⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠉⠀⠀⡸",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⢡⠿⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠓⢄⠀⠀⠀⠀⡰⠁",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⡄⣉⡰⠒⠒⢤⠔⠀⠀⡏⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠜⠀⠀⠀⠀⢹⣍⠏⠁"
        ]
        for i, line in enumerate(art[:17]):
            info = ""
            if i == 5: info = f"                                 User_Name: {usr_name}"
            elif i == 6: info = f"                                 Ram_Total: {ram_total} GB"
            elif i == 7: info = f"                                 Ram_Used:  {ram_used} GB"
            elif i == 8: info = f"                                 Hard_Total:{storage_total} GB"
            elif i == 9: info = f"                                 Hard_Used: {storage_used} GB"
            elif i == 10: info = f"                                Os_Name:   {os_name}"
            elif i == 11: info = f"                               Os_Version:{os_version}"
            elif i == 12: info = f"                             Kernel_Version:{kernel_version}"
            elif i == 13: info = f"                            Now_Time:  {current_time}"
            elif i == 14: info = f"                             Today_Date:{current_date}"
            print(y + line + x + info)

    def img2():
        art = [
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⢠⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠱⡀⠈⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣀⣱⢰⢀⣡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠉⡎⡈⢹⠀⠀⠀⠀⢀⠤⠀⠀⠤⡀⠀⠀",
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⡇⡇⡄⠀⠀⠀⠀⠧⡄⡀⠀⠀⠈⡄⠀",
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⡇⢧⠁⠀⠀⢀⠖⢆⢈⣁⠀⠀⠀⠀⠀",
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⢿⠳⣌⣀⣠⠀⠸⡀⠈⠮⠂⠀⠀⣠⠃⠀",
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⢀⢀⡔⠃⠠⢀⣈⠽⠫⡀⠀⠀⠈⠑⠂⢠⠐⠊⠀⠀⠀",
            r"                                                    ⠀⠀⠀⠰⢲⠤⠭⠕⡤⠈⠑⠒⠆⢤⠤⣠⠿⢭⣗⣄⣀⣂⠆⠀⠀⠀⠀⠀",
            r"                                                    ⠀⢀⠔⠂⠓⢧⢀⣿⠄⣀⡀⠀⠈⠀⠀⢀⣀⣴⣧⡇⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                   ⢀⠔⣟⠲⣀⣄⠘⢳⠅⣉⢰⠀⠂⠈⠁⠒⢎⠁⢰⠜⠋⡆⠀⠀⠀⠀⠀⠀⠀",
            r"                                                   ⢸⠀⠀⠛⠉⠀⠀⢨⠀⠀⠈⠀⠉⠉⠉⠉⠉⣹⠁⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀",
            r"                                                   ⠈⠢⡀⠀⠀⠀⡠⠚⠄⡀⠀⠀⠀⠀⠀⠀⠀⢿⢆⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                    ⠀⠀⠉⠉⠁⠀⠀⠈⣅⣀⣒⡤⠀⠀⠶⠍⡐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢆⠌⠀⠀⠀⠀⢙⠁⠀⠀⠀⠀⠠⠀⠀⠀⠀⠤"
        ]
        for i, line in enumerate(art[:15]):
            info = ""
            if i == 2: info = f"                           User_Name: {usr_name}"
            elif i == 3: info = f"                           Ram_Total: {ram_total} GB"
            elif i == 4: info = f"                           Ram_Used:  {ram_used} GB"
            elif i == 5: info = f"                           Hard_Total:{storage_total} GB"
            elif i == 6: info = f"                           Hard_Used: {storage_used} GB"
            elif i == 7: info = f"                           Os_Name:   {os_name}"
            elif i == 8: info = f"                           Os_Version:{os_version}"
            elif i == 9: info = f"                           Kernel_Version:{kernel_version}"
            elif i == 10: info = f"                           Now_Time:  {current_time}"
            elif i == 11: info = f"                           Today_Date:{current_date}"
            print(y + line + x + info)

    def img3():
        art = [
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⢀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⡇⠀⢈⢻⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⢠⠀⡌⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀⠇⠀⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣀⣸⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢗⠿⠏⠘⠿⢷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⢸⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣇⡖⢺⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢭⣓⠼⠧⢐⣻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⢀⢔⠴⢒⡖⠂⡴⡋⠐⠨⠈⠩⠔⠋⢣⡠⠠⣄⣖⡢⠀⠀⠀⠀⠀",
            r"                                                ⠀⣠⠔⠉⠑⠮⠧⢄⠀⠉⡝⠀⠈⠑⢢⡤⡤⣖⡚⠁⢳⠒⢁⠤⢽⠧⠔⠂⢄⠀",
            r"                                                ⠰⠁⠀⠀⣰⠹⡄⠀⣡⣯⡂⡤⢀⣀⠀⠈⠁⠀⢀⣀⣤⣶⡇⠀⡴⣴⠀⠀⠀⢣",
            r"                                                ⢀⠀⠀⠀⢻⠄⠣⠐⡙⠙⠰⢿⣿⣶⣿⣿⣿⣿⣿⣿⠟⠟⡗⠚⠁⣹⠆⠀⠀⢸",
            r"                                                ⠈⠢⡀⠀⠈⡩⠃⠰⡇⠀⠀⠀⠀⠉⢻⡟⢛⠋⠉⠀⠀⠀⠠⠰⡉⠁⠀⠀⡠⠋",
            r"                                                ⠀⠀⠀⠉⠁⠀⠀⠀⠣⠀⠀⠀⠀⠀⠘⡇⡸⠀⠀⠀⠀⢀⠆⠀⠀⠉⠉⠁⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡖⠀⢹⡶⠖⠬⠴⡖⠞⠁⡖⠁⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢩⡏⠁⠀⠀⠀⠉⢇⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
        ]
        for i, line in enumerate(art[:17]):
            info = ""
            if i == 2: info = f"                             User_Name: {usr_name}"
            elif i == 3: info = f"                             Ram_Total: {ram_total} GB"
            elif i == 4: info = f"                             Ram_Used:  {ram_used} GB"
            elif i == 5: info = f"                             Hard_Total:{storage_total} GB"
            elif i == 6: info = f"                             Hard_Used: {storage_used} GB"
            elif i == 7: info = f"                             Os_Name:   {os_name}"
            elif i == 8: info = f"                             Os_Version:{os_version}"
            elif i == 9: info = f"                             Kernel_Version:{kernel_version}"
            elif i == 10: info = f"                             Now_Time:  {current_time}"
            elif i == 11: info = f"                             Today_Date:{current_date}"
            print(y + line + x + info)

    def img4():
        art = [
            r"                                                        ⠀⠀⠀⠀⠀⢰⣞⣵⠀⢠⡞⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠀⠀⠀⠀⠀⠔⠛⡇⠀⠜⠛⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠀⠀⠀⠀⡜⠀⠀⡇⠎⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠀⠀⠀⢸⠁⠀⢰⢰⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠀⠀⠀⢸⠀⡀⡈⡄⣀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠀⠀⠀⠈⡦⣿⡇⡶⣿⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠀⠀⠀⠀⢠⠀⡇⠆⠁⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠀⠀⠀⡀⠀⠆⢃⣀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠀⠀⠀⠈⢛⠾⡅⠈⢚⠒⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠀⠀⠀⡠⠋⠀⠒⠀⠁⠁⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                   ⢀⣀⡀⢀⡀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠈⣦⢀⣀⠀⠀⣀⠀⠀⠀⠀",
            r"                                                   ⢤⡔⠲⡘⡠⠃⢃⣢⠀⠀⣀⣀⣀⠠⠔⠉⠘⠁⠸⣭⠆⠌⠀⠀⠀⠀",
            r"                                              ⢀⠄⠒⡰⠼⠱⢠⡔⠁⠀⠈⠀⡤⠊⠐⠐⠁⠀⠀⠀⠀⠈⢲⠍⠘⠠⡔⠂⠢⡀",
            r"                                              ⡇⠐⠏⠀⠀⠀⣏⡢⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⠁⠀⠀⠀⡗⠃⠀⢸",
            r"                                              ⢣⠀⠀⠀⠀⡸⢿⣿⣷⣦⣬⢕⣶⣶⢶⣒⣒⣀⣭⣤⡆⢸⠀⠀⠀⠀⠀⠀⠀⢸",
            r"                                               ⠑⠤⠀⠀⢡⠀⠈⠉⠛⢻⠻⠿⠿⠇⡿⠿⠿⠿⠛⠃⠈⠑⢄⠀⠀⠀⢀⠀⠁",
            r"                                                     ⠑⢄⠀⠀⠀⠉⡍⠙⡇⠀⠀⠀⠀⠀⠀⣀⠤⠃⠀⠈⠁⠀⠀⠀",
            r"                                                        ⢫⠄⣐⢠⠴⠤⠽⠤⠤⢠⠀⠀⣈⡹⠀⠀⠀⠀⠀⠀⠀⠀",
            r"                                                        ⠰⡠⠃⠀⠀⠀⠀⠀⠀⠀⠉⢅⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀"
        ]
        for i, line in enumerate(art[:19]):
            info = ""
            if i == 5: info = f"                             User_Name: {usr_name}"
            elif i == 6: info = f"                             Ram_Total: {ram_total} GB"
            elif i == 7: info = f"                             Ram_Used:  {ram_used} GB"
            elif i == 8: info = f"                             Hard_Total:{storage_total} GB"
            elif i == 9: info = f"                             Hard_Used: {storage_used} GB"
            elif i == 10: info = f"                              Os_Name:   {os_name}"
            elif i == 11: info = f"                              Os_Version:{os_version}"
            elif i == 12: info = f"                               Kernel_Version:{kernel_version}"
            elif i == 13: info = f"                               Now_Time:  {current_time}"
            elif i == 14: info = f"                               Today_Date:{current_date}"
            print(y + line + x + info)



    def main_menu():
        print(colors["Cyan"] + '[01] Random Word List')
        print(colors["Cyan"] + '[02] Wordlist with Victim Information')
        print(colors["Cyan"] + '[03] Exit')
        return input(colors["Yellow"] + '[?] Enter Number For Select Option: ')
    def sub_menu():
        print(colors["Cyan"] + '[01] Random Range')
        print(colors["Cyan"] + '[02] Provide Number of Character')
        print(colors["Cyan"] + '[03] Provide Start & End Value')
        return input(colors["Yellow"] + '[?] Enter Number For Select Option: ')

    def get_charset():
        char = ''
        char_low = 'abcdefghijklmnopqrstuvwxyz'
        char_up = char_low.upper()
        char_spec = r'!\][/?.,~-=";:><@#$%&*()_+\' '
        char_num = '0123456789'
        return char, char_low, char_up, char_spec, char_num

    def get_custom_charset():
        char, char_low, char_up, char_spec, char_num = get_charset()
        spec = input(colors["Yellow"] + '[?] Do You Want Special Characters? [Y/n]: ').lower()
        low = input(colors["Yellow"] + '[?] Do You Want Lowercase? [Y/n]: ').lower()
        up= input(colors["Yellow"] + '[?] Do You Want Uppercase? [Y/n]: ').lower()
        num = input(colors["Yellow"] + '[?] Do You Want Numeric Characters? [Y/n]: ').lower()
        
        charset = char
        if spec == 'y':
            charset += char_spec
        if low == 'y':
            charset += char_low
        if up == 'y':
            charset += char_up
        if num == 'y':
            charset += char_num
        return charset

    def get_victim_charset():
        char, char_low, char_up, char_spec, char_num = get_charset()
        print(colors["Cyan"] + "\n[!] Enter Victim Information")
        f_n = input('[*] First Name: ')
        m_n = input('[*] Middle Name: ')
        l_n = input('[*] Last Name: ')
        b_d = input('[*] Birth Date: ')
        b_m = input('[*] Birth Month: ')
        b_y= input('[*] Birth Year: ')

        victim = f_n + m_n + l_n + b_d + b_m + b_y
        spec = input(colors["Yellow"] + '[?] Do You Want Special Characters? [Y/n]: ').lower()
        low = input(colors["Yellow"] + '[?] Do You Want Lowercase? [Y/n]: ').lower()
        up= input(colors["Yellow"] + '[?] Do You Want Uppercase? [Y/n]: ').lower()
        num = input(colors["Yellow"] + '[?] Do You Want Numeric Characters? [Y/n]: ').lower()

        charset = victim
        if spec == 'y':
            charset += char_spec
        if low == 'y':
            charset += char_low
        if up == 'y':
            charset += char_up
        if num == 'y':
            charset += char_num
        return charset    


    def sub():
        main_choice = main_menu()
        if main_choice in ['1', '2']:
            sub_choice = sub_menu()
            if main_choice == '1':
                charset = get_custom_charset()
            elif main_choice == '2':
                charset = get_victim_charset()

            file_name = input(colors['Yellow'] + '[!] Insert a name for your wordlist file: ')
            with open(file_name, 'w') as f:
                        if sub_choice == '1':
                            num_words = int(input(colors['Yellow'] + '[!] Enter How Many Words You Want: '))
                            min_len = 5
                            max_len = 15
                            for _ in range(num_words):
                                length = random.randint(min_len, max_len)
                                password = ''.join(random.choices(charset, k=length))
                                line = password
                                f.write(line + '\n')
                        
                        elif sub_choice == '2':
                            length = int(input(colors['Yellow'] + '[!] Enter How Many Characters You Want: '))
                            num_words = int(input(colors['Yellow'] + '[!] Enter How Many Words You Want: '))
                            for _ in range(num_words):
                                password = ''.join(random.choices(charset, k=length))
                                line = password
                                f.write(line + '\n')
                        
                        elif sub_choice == '3':
                            scale = input(colors['Yellow'] + 'Provide a size scale [eg: "1 to 8" = 1:8]: ')
                            start, end = map(int, scale.split(':'))
                            for length in range(start, end + 1):
                                for combo in itertools.product(charset, repeat=length):
                                    password = ''.join(combo)
                                    line = password
                                    f.write(line + '\n')
                        else:
                            print(colors["Red"] + "Invalid Option! Please select 1-3")
                            return sub()
        elif main_choice == '3':
            print(colors["Red"] + 'Your Exit')
            print(colors["Green"] + 'Good Bye..')
            exit()
        else:
            print(colors["Red"] + "Invalid Option! Please select 1-2")
            return sub()
        num = main1()
    if num == 0:
        img1()
    elif num == 1:
        img2()
    elif num == 2:
        img3()
    else:
        img4()
    
    # Start wordlist generator
    sub()

if __name__ == "__main__":
    main()
