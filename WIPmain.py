# J Pickin & T Trotman
# Richard Challoner School
# 21 Sep 2021
# LoginTXT Codding Challenge

## Importing socket and time for use in the program
import socket
import time
from colorama import Fore, Back, Style

loggedOut = True
attempts = 4
ip = socket.gethostbyname(socket.gethostname())
device = socket.gethostname()


def menu():
    print("________________________________")
    print("Welcome to the Automated Reader for Securely Encrypted Stuff")
    print("________________________________")


def tshcbActivated():
    print(Fore.RED + "THERMONUCLEAR HYDROCHLORIC SULFURIC CLUBHOUSE BOMB LAUNCHING IN 3 SECONDS.")
    time.sleep(1)
    print(Fore.RED + "THERMONUCLEAR HYDROCHLORIC SULFURIC CLUBHOUSE BOMB LAUNCHING IN 2 SECONDS.")
    time.sleep(1)
    print(Fore.RED + "THERMONUCLEAR HYDROCHLORIC SULFURIC CLUBHOUSE BOMB LAUNCHING IN 1 SECOND.")
    time.sleep(1)
    location = 2000
    while location >= 1000:
        speed = (location / 200000)
    print(Fore.RED + "DISTANCE: " + str(location) + "m")
    if speed <= 0:
        speed = 0.0000000000001
    time.sleep(speed)
    location = location - 1
    while location <= 1000:
        speed = location / 200000
        print(Back.RED + Fore.BLACK + "DISTANCE: " + str(location) + "m")
        time.sleep(speed)
        location = location - 1
    if location <= 25:
        for x in range(100):
            print(
                "ÿØÿà JFIF  H H  ÿá Exif  MM *           1      V2      t‡i      ˆê      J    ê         - 2 7 ; @ E J O T Y ^ c h m r w |  † ‹  • š Ÿ ¤ © ® ² · ¼ Á Æ Ë Ð Õ Û à å ë ð ö û%+28>ELRY`gnu|ƒ‹’š¡©±¹ÁÉÑÙáéòú&/8AKT]gqz„Ž˜¢¬¶ÁËÕàëõ !-8COZfr~Š–¢®ºÇÓàìù -;HUcq~Œš¨¶ÄÓáðþ+:IXgw†–¦µÅÕåö7HYj{Œ¯ÀÑãõ+=Oat†™¬¿Òåø2FZn‚–ª¾Òçû		%	:	O	d	y		¤	º	Ï	å	û")
            exit()


def loginInput():
    global attempts
    usernameAttempt = input("Please enter your username: ")
    passwordAttempt = input("Please enter your password: ")
    if usernameAttempt != "username" and passwordAttempt != "password":
        attempts = attempts - 1
        if attempts == 0:
            tshcbActivated()
        print("You have entered an incorrect username or password. Please try again. " + str(
            attempts) + " attempts remain.")
        print("")
    else:
        loggedOut = False


menu()

while loggedOut == True and attempts != 0:
    loginInput()

if not loggedOut:
    print("________________________________")
    print("User Authenticated")
    print("________________________________")
    document = input("What is the name of the document you would like to load? ")
    if document == "private":
        t = open("private.txt", "r")
        print(t.read())

while loggedOut == True and attempts != 0:
    loginInput