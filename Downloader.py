from os import name, system
from pathlib import Path
from random import choice
from string import ascii_letters, digits
from sys import exit, stdout
from time import sleep

from colorama import Fore
from requests import get


def start_script():
        
    system('cls' if name == 'nt' else 'clear')
    # info
    script_version  = '1.1'
    coder = "ALIILAPRO From IRAN"
    telegram_id = "aliilapro"
    channel = "Source-Pro"
    # Script banner
    banner = f'''

  _    _                 _           _       _____                      _                 _           
 | |  | |               | |         | |     |  __ \                    | |               | |          
 | |  | |_ __  ___ _ __ | | __ _ ___| |__   | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 | |  | | '_ \/ __| '_ \| |/ _` / __| '_ \  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |__| | | | \__ \ |_) | | (_| \__ \ | | | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \____/|_| |_|___/ .__/|_|\__,_|___/_| |_| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                  | |                                                                                 
                  |_|  Version_{script_version} -- Coder >> {coder} -- Telegram >> {telegram_id}
                       Channel Telegram >> {channel}
                       
                       About Script::>
                       
                        *  With this script, you can download wallpaper
                        *  from "unsplash.com" by giving it a keyword,
                        *  then it downloads a random image with that keyword.                                                                                                      
               '''
    
    print(Fore.LIGHTRED_EX + banner)
    
    print("\n\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX + "Note" + Fore.LIGHTGREEN_EX + "]" +
          Fore.RESET + " Press Ctrl + C To Exit.\n")

def genString(stringLength):
    
    letters = ascii_letters + digits
    
    return ''.join(choice(letters) for i in range(stringLength))

def req(url):
    
    try:
        
        r = get(url)
        
    except:
        
        r = get(url)
        
    return r

def search_animation(percent):

    animation = list(range(percent))
    
    # animation.reverse()
    
    for r in range(len(animation)):
        
        sleep(0.1)
        
        stdout.write("\r" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTGREEN_EX + "] " + 
                     Fore.LIGHTCYAN_EX + "Sarching {}%".format(animation[r % len(animation)]))

        stdout.flush()
    
    print("\n\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX +"+" + Fore.LIGHTGREEN_EX +"]" + 
          Fore.LIGHTCYAN_EX + " Downloading... ")
    
def download():
    
    try:
        
        start_script()
        # Enter your desired keyword
        kword = input("\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX +"+" + Fore.LIGHTGREEN_EX +"]" + 
                      Fore.LIGHTCYAN_EX + " Enter Your KEYWORD (e.g. flower,sun) >> ")
        # More sizes can be add later
        print("\n\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX + "+" + Fore.LIGHTGREEN_EX + "]" + 
              Fore.LIGHTCYAN_EX + " Sizes:" + Fore.LIGHTWHITE_EX + "\n\n\t[1] 1920x1080\n" + "\n\t[2] 1600x900\n" + "\n\t[3] 800x600")
        
        img_size = input("\n\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX + "+" + Fore.LIGHTGREEN_EX + "]" +
              Fore.LIGHTCYAN_EX + " Pick Image Size (Enter Its Number - Default: 1920) >> ")
        
        print("\n")
        
        if img_size == 1:
            
            RES_URL = "1920x1080"
        
        elif img_size == 2:
            
            RES_URL = "1600x900"
            
        elif img_size == 3:
            
            RES_URL = "800x600"
       
        else:
            
            RES_URL = "1920x1080"
        # Changed ./wp to ./Downloads
        DOWNLOAD_FOLDER = './Downloads'
        # Changed filename with entered kewword and a random digits-ascii_letters and changed file suffix to .png
        FILE_NAME = '{}_{}_{}.png'.format(kword.capitalize(), RES_URL ,genString(7))
        
        FILE_PATH = '{}/{}'.format(DOWNLOAD_FOLDER, FILE_NAME)

        BASE_URL = 'https://source.unsplash.com'

        URL = '{}/{}/?{}'.format(BASE_URL, RES_URL, kword)
        
        Path(DOWNLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
        # Searching status
        search_animation(101)
            
        img_data = req(URL).content
            
        with open(FILE_PATH, 'wb') as handler:
                
            handler.write(img_data)
        
        print("\n\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX + "+" + Fore.LIGHTGREEN_EX + "]" + 
              Fore.LIGHTCYAN_EX + " Wallpaper "+Fore.LIGHTWHITE_EX+"[{}]".format(FILE_NAME)+ Fore.LIGHTCYAN_EX+" Successfully Saved In Downloads Folder.\n\n")
        
        input("\n\n" + Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"+"+ Fore.LIGHTGREEN_EX+"] "+
              Fore.LIGHTRED_EX+"Press ENTER To Back To Menu... ")
        
    except Exception as error:
        
        e = str(error)
           
        print("\n\n" + Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"!"+ Fore.LIGHTGREEN_EX+"] "+ 
              Fore.LIGHTRED_EX+"Error >>" + Fore.LIGHTWHITE_EX + f" {e}")
           
        input("\n\n" + Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"+"+ Fore.LIGHTGREEN_EX+"] "+
              Fore.LIGHTRED_EX+"Press ENTER To Back To Menu... ")
    
    except KeyboardInterrupt:
        
        system("cls" if name == "nt" else "clear")
        
        exit()
    
def start():
    
    while True:
       
       try:
           
           start_script()
           
           user_input = input("\n\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX +"?" + Fore.LIGHTGREEN_EX +"]" + 
                              Fore.LIGHTCYAN_EX + " Do You Want To Download A New Wallpaper? (Y/n - Default: YES) >> ")
        
           if user_input.lower() == "y":
               
               download()
        
           elif user_input.lower() == "n":
               
               system("cls" if name == "nt" else "clear")
               
               break
           
           else:
               
               download()
               
       except Exception as error:
           
           e = str(error)
           
           print("\n\n" + Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"!"+ Fore.LIGHTGREEN_EX+"] "+ 
                 Fore.LIGHTRED_EX+"Error >>" + Fore.LIGHTWHITE_EX + f" {e}")
           
           input("\n\n" + Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"+"+ Fore.LIGHTGREEN_EX+"] "+
                 Fore.LIGHTRED_EX+"Press ENTER To Back To Menu... ")
       
       except KeyboardInterrupt:
           
           system("cls" if name == "nt" else "clear")
           
           break
        
if __name__ == "__main__":
        
    start()
