import datetime
import platform
import time
import os
import urllib.request
import logging
import sys
import subprocess

OS='Darwin'

HelpFile = open("HELP.txt", "w")

#This is for the user to know what programs are used in this program
ProgramsUsed = "+++++++++++++++Programs used+++++++++++++++"
ProgramsUsedInfo = "This program will help you crack passwords \nIt has two programs inside it, one is Hydra and the other is Nmap"

#this is for the user to understand what the program does
HowToUse = "\n+++++++++++++++How to use++++++++++++++++++"
HowToUseInfo01 = "To use the program you have to tell the computer what port you want to scan."
HowToUseInfo02 = "\nIt will then scan the port that you asked for on the network and see if any ports that you asked are open."
HowToUseInfo03 = "\nIf there are any ports that are open, it will ask for a username and hostname"
HowToUseInfo04 = "\nWhen you give the program the username and hostname, it will try to crack that given parameters you gave it."

GREEN = "\033[92m"
RESET = "\033[0m"

#this is for the user to understand what the program does
if len(sys.argv) == 2 and sys.argv[1] == "--help" or len(sys.argv) == 2 and sys.argv[1] == "-h":
    subprocess.run(["figlet", "? HELP ?"])
    text_art = """
 ___   _   _ _____ _     ____    ___ 
|__ \ | | | | ____| |   |  _ \  |__ \\
  / / | |_| |  _| | |   | |_) |   / /
 |_|  |  _  | |___| |___|  __/   |_|
 (_)  |_| |_|_____|_____|_|      (_)  
"""
    print(text_art, file=HelpFile)
    print()
    #inputs the program used logo in a help file
    print(ProgramsUsed, file=HelpFile)

    #puts the info about the program inside the help file
    print(ProgramsUsedInfo, file=HelpFile)
    print("+++++++++++++++Programs used+++++++++++++++")
    print("This program will help you crack passwords")
    print("It has two programs inside it, one is Hydra and the other is Nmap")
    print()

    #Puts the info logo in the help file
    print(file=HelpFile)
    print(HowToUse, file=HelpFile)

    #puts the info about how to use the program inside the help file
    print(HowToUseInfo01, 
          HowToUseInfo02, 
          HowToUseInfo03,
          HowToUseInfo04,
          file=HelpFile)
    print("+++++++++++++++How to use++++++++++++++++++")
    print("To use the program you have to tell the computer what port you want to scan.")
    print("It will then scan the port that you asked for on the network and see if any ports that you asked are open.")
    print("If there are any ports that are open, it will ask for a username and hostname.")
    print("When you give the program the username and hostname, it will try to crack that given parameters you gave it.")
    print()
else:
    # gets the current time and formats it HH:MM:SS
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%I:%M:%S %p")

    # Get the current date
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")

    # easy way to read the root user function
    root = 0

    # makes the log file accessible to read for the user and developer
    logging.basicConfig(filename="ERROR.log", level=logging.ERROR)

    def connect(host="google.com"):
        try:
            urllib.request.urlopen("http://" + host)  # Try to open a connection to the host
            return True  # If successful, return True
        except:
            return False  # If unsuccessful, return False


    if connect() == True:  # Makes sure that the user is connected to the internet
        if platform.system() == OS:  # Check if the current OS is macOS
            if os.geteuid() == root:  # Check if running as root
                def print_loading_bar(iterations, delay=0.1, width=40):
                    """
                    Prints a loading bar with green dots to visualize progress.
                    
                    Args:
                        iterations (int): Total number of iterations.
                        delay (float, optional): Delay between updates in seconds. Default is 0.1 seconds.
                        width (int, optional): Width of the loading bar. Default is 40 characters.
                    """
                    for loadingBar in range(iterations + 1):
                        progress = loadingBar / iterations  # Calculate the progress ratio
                        bar_length = int(progress * width)  # Calculate the number of dots for the current progress
                        bar = GREEN + '•' * bar_length + RESET + ' ' * (width - bar_length)  # Construct the loading bar string
                        percentage = int(progress * 100)  # Calculate the percentage of completion
                        
                        # Print the loading bar and percentage, replacing the line each iteration
                        print(f'\r[{bar}] {percentage}% ', end='', flush=True)
                        
                        time.sleep(delay)  # Pause to control the update rate
                print_loading_bar(50)
                os.system("bash script.sh")  # Replace with your actual script to run after loading
            else:
                logging.critical(f"TIME:{formatted_time} Please run as root. DATE:{current_date}")
                print(f"TIME:{formatted_time} Please run as root. DATE:{current_date}")
        else:
            logging.warning(f"TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}")
            print(f"TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}")
    else:
        logging.critical(f"TIME:{formatted_time} You are offline. Please connect to the internet. DATE:{current_date}")
        print(f"TIME:{formatted_time} You are offline. Please connect to the internet. Date:{current_date}")