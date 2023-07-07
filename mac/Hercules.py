import datetime
import platform
import time
import os
import urllib.request
import logging

from tqdm import tqdm

current_time = datetime.datetime.now().time()
formatted_time = current_time.strftime("%I:%M:%S %p")

# Get the current date
current_date = datetime.datetime.now().strftime("%m/%d/%Y")

root = 0

def connect(host="google.com"):
    try:
        urllib.request.urlopen("http://" + host)  # Try to open a connection to the host
        return True  # If successful, return True
    except:
        return False  # If unsuccessful, return False

if connect():
    if platform.system() == "Darwin":  # Check if the current OS is macOS
        if os.geteuid() == root:  # Check if running as root
            for _ in tqdm(range(100), ascii=False, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', colour="green", desc="Loading Hercules"):
                time.sleep(0.1)  # Simulate loading delay
            os.system("bash script.sh")  # Replace with your actual script to run after loading
        else:
            logging.error(f"{formatted_time} Please run as root. DATE:{current_date}")
    else:
        logging.warning(f"{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}")
else:
    logging.error(f"{formatted_time} You are offline. Please connect to the internet. DATE:{current_date}")

