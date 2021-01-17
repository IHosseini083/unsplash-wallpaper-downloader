from os import name, system
from pathlib import Path
from random import choice
from string import ascii_letters, digits
from sys import exit
from time import sleep

from colorama import Fore, init
from requests import get

init()

class TMPrinter():
    
    def __init__(self):
    
        self.max_len = 0

    def out(self, text):
    
        if len(text) > self.max_len:
    
            self.max_len = len(text)
    
        else:
    
            text += (" " * (self.max_len - len(text)))
    
        print(text, end='\r')
        
def script_banner():
        
    system('cls' if name == 'nt' else 'clear')

    script_version  = '2.0'
    coder = "ALIILAPRO From IRAN"
    telegram_id = "aliilapro"
    channel = "Source-Pro"

    banner = f'''

  _    _                 _           _       _____                      _                 _           
 | |  | |               | |         | |     |  __ \                    | |               | |          
 | |  | |_ __  ___ _ __ | | __ _ ___| |__   | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 | |  | | '_ \/ __| '_ \| |/ _` / __| '_ \  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |__| | | | \__ \ |_) | | (_| \__ \ | | | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \____/|_| |_|___/ .__/|_|\__,_|___/_| |_| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                  | |                                                                                 
                  |_|  Version >> {script_version} -- Coder >> {coder} -- Telegram >> {telegram_id}
                       Channel Telegram >> {channel}
                       
                       About Script::>
                       
                        *  With this script, you can download wallpaper
                        *  from "unsplash.com" by giving it a keyword,
                        *  then it downloads a random image with that keyword.                                                                                                      
               '''
    
    print(Fore.LIGHTRED_EX + banner)
    
    print("\n\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX + "Note" + Fore.LIGHTGREEN_EX + "]" +
          Fore.LIGHTRED_EX + " Press Ctrl + C To Exit.\n")

def genString(stringLength):
    
    letters = ascii_letters + digits
    
    return ''.join(choice(letters) for i in range(stringLength))

def req(url):
    
    try:
        
        r = get(url)
        
    except:
        
        r = get(url)
        
    return r
    
def download():
    
    try:
        
        printout = TMPrinter()
        
        script_banner()
        # Enter your desired keyword
        KEYWORDS = input("\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX +"+" + Fore.LIGHTGREEN_EX +"]" + 
                      Fore.LIGHTCYAN_EX + " Enter Your KEYWORDS With Comma [e.g. flower,sun,...] >> "+Fore.LIGHTWHITE_EX+"").split(",")
       
        print("\n")
       
        RES_URL = "1920x1080"    
        # Changed ./wp to ./Downloads
        DOWNLOAD_FOLDER = './Downloads'

        BASE_URL = 'https://source.unsplash.com'
        
        for kword in KEYWORDS:    
            # Changed filename with entered kewword and a random digits-ascii_letters and changed file suffix to .png            
            FILE_NAME = '{}-{}-{}.png'.format(kword.capitalize(), RES_URL ,genString(7))
                
            FILE_PATH = '{}/{}'.format(DOWNLOAD_FOLDER, FILE_NAME)

            URL = '{}/{}/?{}'.format(BASE_URL, RES_URL, kword)
                
            Path(DOWNLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
                
            printout.out(Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX +"+" + Fore.LIGHTGREEN_EX +"]" + 
                         Fore.LIGHTCYAN_EX + " Searching"+Fore.LIGHTWHITE_EX+f" [{kword}] "+Fore.LIGHTCYAN_EX+"... ")
                
            sleep(5)
                
            printout.out(Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX +"+" + Fore.LIGHTGREEN_EX +"]" + 
                         Fore.LIGHTCYAN_EX + " Downloading"+Fore.LIGHTWHITE_EX+f" [{kword}] "+Fore.LIGHTCYAN_EX+"... ")
                    
            img_data = req(URL).content               
                    
            with open(FILE_PATH, 'wb') as handler:
                        
                handler.write(img_data)
                    
            printout.out(Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX +"+" + Fore.LIGHTGREEN_EX +"]" + 
                         Fore.LIGHTCYAN_EX + " Downloaded ! ")            
                
            sleep(4)
                
            printout.out(Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX + "+" + Fore.LIGHTGREEN_EX + "]" + 
                         Fore.LIGHTCYAN_EX + " Wallpaper "+Fore.LIGHTWHITE_EX+"[{}]".format(FILE_NAME)+ Fore.LIGHTCYAN_EX+" Successfully Saved In Downloads Folder.")
                
            print(Fore.LIGHTBLACK_EX+"\n\n -------------------------------------------------------- \n\n")
            
        input("\n" + Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"+"+ Fore.LIGHTGREEN_EX+"] "+
              Fore.LIGHTRED_EX+"Press ENTER To Back To Menu... ")
        
    except Exception as error:
        
        printout = TMPrinter()
        
        e = str(error)
        
        if "connection failed" in e:
                
            printout.out(Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"!"+ Fore.LIGHTGREEN_EX+"] "+ 
                         Fore.LIGHTRED_EX+"Error >>" + Fore.LIGHTWHITE_EX + " Please Check Your Connection ! Or You May Use A VPN.")    
       
        else:
           
            printout.out(Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"!"+ Fore.LIGHTGREEN_EX+"] "+ 
                         Fore.LIGHTRED_EX+"Error >>" + Fore.LIGHTWHITE_EX + f" {e}")
           
        input("\n\n" + Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"+"+ Fore.LIGHTGREEN_EX+"] "+
              Fore.LIGHTRED_EX+"Press ENTER To Back To Menu... ")
    
    except KeyboardInterrupt:
        
        system("cls" if name == "nt" else "clear")
        
        exit()
    
def start():
    
    while True:
       
       try:
           
           script_banner()
           
           user_input = input("\n\n" + Fore.LIGHTGREEN_EX + " [" + Fore.LIGHTYELLOW_EX +"?" + Fore.LIGHTGREEN_EX +"]" + 
                              Fore.LIGHTCYAN_EX + " Do You Want To Download A New Wallpapers? [Y/n - Default: YES] >> "+Fore.LIGHTWHITE_EX+"")
        
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
           
           input("\n" + Fore.LIGHTGREEN_EX+" ["+Fore.LIGHTYELLOW_EX+"+"+ Fore.LIGHTGREEN_EX+"] "+
                 Fore.LIGHTRED_EX+"Press ENTER To Back To Menu... ")
       
       except KeyboardInterrupt:
           
           system("cls" if name == "nt" else "clear")
           
           break

if __name__ == "__main__":
        
    start()
