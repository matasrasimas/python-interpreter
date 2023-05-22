import basic
import os

while True:
    text = input('\033[38;5;82mradiatorius > \033[0m')

    if text == 'exit':
        exit()

    if text == 'clear' or text == 'clr':
         os.system('cls') # clear the console when user inputs "clear" or "clr"
         continue   

    result, error = basic.run('<stdin>', text)

    if error:
         print('\033[38;5;196m' + error.as_string() + '\033[0m')
    


