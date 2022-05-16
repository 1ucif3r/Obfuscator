from importlib.resources import contents
import os
import base64
from sys import argv
from genericpath import isfile
from traceback import print_tb
from pystyle import *


def clear_console():
    os.system('cls')


clear_console()

banner1 = r"""

 _,.
     ,` -.)
    ( _/-\\-._
   /,|`--._,-^|            ,
   \_| |`-._/||          ,'|
     |  `-, / |         /  /
     |     || |        /  /
      `r-._||/   __   /  /
  __,-<_     )`-/  `./  /
 '  \   `---'   \   /  /
|    |           |./  /
|    /           //  /
 \_/' \         |/  /
  |    |   _,^-'/  /
  |    , ``  (\/  /_
   \,.->._    \X-=/^
   (  /   `-._//^`
    `Y-.____(__}
     |     {__)
           () 

           """


banner2 = r'''


      ▄▄▄▄· ·▄▄▄▄• ▄▌.▄▄ ·  ▄▄·  ▄▄▄· ▄▄▄▄▄      ▄▄▄  
▪     ▐█ ▀█▪▐▄▄·█▪██▌▐█ ▀. ▐█ ▌▪▐█ ▀█ •██  ▪     ▀▄ █·
 ▄█▀▄ ▐█▀▀█▄██▪ █▌▐█▌▄▀▀▀█▄██ ▄▄▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█▌.▐▌██▄▪▐███▌.▐█▄█▌▐█▄▪▐█▐███▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
 ▀█▄▀▪·▀▀▀▀ ▀▀▀  ▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀                                                            
 
'''

lucifer = r'''

    BY :

 ▄█       ███    █▄   ▄████████  ▄█     ▄████████    ▄████████    ▄████████ 
███       ███    ███ ███    ███ ███    ███    ███   ███    ███   ███    ███ 
███       ███    ███ ███    █▀  ███▌   ███    █▀    ███    █▀    ███    ███ 
███       ███    ███ ███        ███▌  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███       ███    ███ ███        ███▌ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███       ███    ███ ███    █▄  ███    ███          ███    █▄  ▀███████████ 
███▌    ▄ ███    ███ ███    ███ ███    ███          ███    ███   ███    ███ 
█████▄▄██ ████████▀  ████████▀  █▀     ███          ██████████   ███    ███ 
▀                                                                ███    ███ 
                                                    
 
'''

System.Size(140, 40)
System.Title("Obfuscator")
System.Clear()
Anime.Fade(Center.Center(lucifer), Colors.red_to_green, Colorate.Vertical, interval=0.025, enter=True)


banner = Add.Add(banner1, banner2, center=True)

def stage(text: str) -> str:
    return print(f"""{Col.Symbol('...', Col.cyan, Col.red)} {Col.cyan}{text}{Col.reset}""")


print(Colorate.Diagonal(Colors.blue_to_cyan, Center.XCenter(banner + '\n\n')))


# configuration
OFFSET = 10
VARIABLE_NAME = '__0x_1ucif3r' * 100

def obfuscate(content):

    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code




def main():
   
    try:
        print("                                                                                                           ")
        
        path = input(f"{Col.Symbol('?', Col.cyan, Col.red)} {Col.cyan}Drag a file to Obfuscate {Col.red}-> {Col.reset}")
        print()
        if not isfile(path):
            input(f"""{Col.Symbol('!', Col.red, Col.red)} {Col.red}Error: {Col.Symbol(path, Col.light_red, Col.red, "'", "'")}{Col.cyan} doesn't exist!{Col.reset}""")
            exit()
        if not os.path.exists(path):
            print('[-] File not found')
            exit()

        if not os.path.isfile(path) or not path.endswith('.py'):
            print('[-] Invalid file')
            exit()
        
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()

        obfuscated_content = obfuscate(file_content)

        with open(f'{path.split(".")[0]} (obfuscated).py', 'w') as file:
            file.write(obfuscated_content)

        print('[+] Script has been obfuscated')
    except:
        print(f'Error : Check The Filename or FileLocation Properly')

if __name__ == '__main__':
    main()