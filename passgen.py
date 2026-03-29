import time
import secrets
import string
# import os     ###still on the fence about the screen clear as it clears everthing in the terminal so you loose scrollable history there

def print_banner():
    banner = r"""
           *~~~\_._/~*       
          *~  ( o o )  ~*    
         *~   (  -  )   ~*  
        **~~~o("===")o~~~**   
       *\/\/\/\/\/\/\/\/\/ *

            BRYNN-P
        Password_generator            
"""
    lines = banner.strip("\n").split("\n")

    for line in lines:
        print(line)
        time.sleep(0.1)
    time.sleep(1)
    # os.system('cls||clear') # thank you stackoverflow for this elegant little peice 

def intro():
    info = r"""
        welcome to the password generator
There are a few rules when it comes to making passwords
1. Passwords should be atleast 16 characters long
2. Passwords should be random (not your dogs name)
3. Passwords should contain a mix of UPPERCASE, lowercase and symbols 

There are strong passwords, and weak passwords
There are no uncrackable passwords!

    """
    info = info.strip("\n").split("\n")
    for line in info:
        print(line)
        time.sleep(0.3)
    time.sleep(1.5)
  #  os.system('cls||clear')

def passwords():
  while True:
        password_type = input("what type of password do you want to create.\nPlease choose one of the numbers below.\n1. Mix Char 7 characters?\n2. Mix char 10 characters\n3. Mix char 16 characters\n")
        if password_type == "1" or password_type == "2":
            print("nope lets try again")
            time.sleep(1)
            intro()
        elif password_type == "3":
            print("this is where i can now start working\nI will keep building this out so that you can set your own password length\nwithin the rules ofcourse.")
            
            while True:
                pas_length = input("How long would you like your password to be? ")
                try:
                    pas_len = int(pas_length)
                    if pas_len >= 16:
                        break
                    else:
                        print("That needs to be 16 or greater please")
                except ValueError:
                    print("Come now, we said numbers, what are you trying?")
                    time.sleep(0.5)
                    print("Maybe i must be more specific")
                    time.sleep(0.5)
                    print("please use an int that is 16 or greater")
                    time.sleep(0.5)
            upper = string.ascii_uppercase
            lower = string.ascii_lowercase
            digit = string.digits
            punct = string.punctuation

            pass_char = [
                secrets.choice(upper),
                secrets.choice(lower),
                secrets.choice(digit),
                secrets.choice(punct)
            ]
            all_char = upper + lower + digit + punct
            for _ in range(pas_len-4):
                pass_char.append(secrets.choice(all_char))
            secrets.SystemRandom().shuffle(pass_char)
            return ''.join(pass_char)
        
        else:
            print("Well I never, how did you end up here\nO well as you wish\nSystem removing system 32: Do not shut down or restart!")
            time.sleep(2.5)
            print("Im just messing with you =+)")
            time.sleep(0.5)
            print("But the guy who wrote this program is still building this project out")
            time.sleep(0.5)
            print("and they have not writen more in for this so bye for now")
            break

if __name__ == "__main__":
    print_banner()
    print("")
    intro()
    print(passwords())