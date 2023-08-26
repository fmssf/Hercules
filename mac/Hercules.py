import datetime
import platform
import time
import os
import urllib.request
import logging
import sys
import subprocess

GREEN = "\033[92m"
RESET = "\033[0m"

#this is for the user to understand what the program does
if len(sys.argv) == 2 and sys.argv[1] == "--help" or len(sys.argv) == 2 and sys.argv[1] == "-h":
    subprocess.run(["figlet", "? HELP ?"])
    print()
    print("+++++++++++++++Programs used+++++++++++++++")
    print("This program will help you crack passwords")
    print("It has two programs inside it, one is Hydra and the other is Nmap")
    print()
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
        if platform.system() == "Darwin":  # Check if the current OS is macOS
            if os.geteuid() == root:  # Check if running as root
                def print_loading_bar(iterations, delay=0.1, width=40):
                    for i in range(iterations + 1):
                        progress = i / iterations
                        bar_length = int(progress * width)
                        bar = GREEN + '•' * bar_length + RESET + ' ' * (width - bar_length)
                        percentage = int(progress * 100)
                        
                        print(f'\r[{bar}] {percentage}% ', end='', flush=True)
                        time.sleep(delay)
                # Usage
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