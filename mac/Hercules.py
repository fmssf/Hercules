from DontEdit import *
from HelpLogo import *

# gets the current time and formats it HH:MM:SS
current_time = datetime.datetime.now().time()

#get the current time and formats it in the 12 hour format
formatted_time = current_time.strftime("%I:%M:%S %p")

# Get the current date
current_date = datetime.datetime.now().strftime("%m/%d/%Y")

ERROR = open("ERROR.log", "a")

ProgramName = "Hercules"
SoftwareName = "Hercules.py"  

#this is for the user to understand what the program does
def show_help():

    HelpFile = open("HELP.txt", "w")

    #This is for the user to know what programs are used in this program
    ProgramsUsed = f"+++++++++++++++PROGRAMS USED+++++++++++++++"
    ProgramsUsedInfo01 = f"\nThis program will help you crack passwords"
    ProgramsUsedInfo02 = f"\nIt has two programs inside it"
    ProgramsUsedInfo03 = f"\none is {GREEN}Hydra{RESET} and the other is {GREEN}Nmap{RESET} and"

    #this is for the user to understand what the program does
    HowToUse = f"\n+++++++++++++++HOW TO USE++++++++++++++++++"
    HowToUseInfo01 = f"\nTo use the program you have to tell the computer what port you want to scan."
    HowToUseInfo02 = f"\nIt will then scan the port that you asked for on the network and see if any ports that you asked are open."
    HowToUseInfo03 = f"\nIf there are any ports that are open, it will ask for a username and hostname"
    HowToUseInfo04 = f"\nWhen you give the program the username and hostname, it will try to crack that given parameters you gave it."
    HowToUseInfo05 = f"\nIf you want to use the program on a global network, you can type {GREEN}'sudo python3 {SoftwareName} {GLOBAL}'{RESET}"
    HowToUseInfo06 = f"\nIf you want to use the program with GUI support you can type {GREEN}'sudo python3 {SoftwareName} {GUI}'{RESET}" 
    HowToUseInfo07 = f"\nIf you want to use the program locally, you can type {GREEN}'python3 {SoftwareName} {LOCAL}'{RESET}"
    HowToUseInfo08 = f"\nIf you want to use the program with GUI in Local mode you can type {GREEN}'python3 {SoftwareName} {GuiLocal}'{RESET}"
    HowToUseInfo09 = f"\nIf you want to have the program install required packages by it's self type {GREEN}'python3 {SoftwareName} {installRequirement}'{RESET}"
    HowToUseInfo10 = f"\nIf you want to have the program uninstall required packages by it's self type {GREEN}'python3 {SoftwareName} {uninstallRequirement}'{RESET}"

    
    ProgramsUSED = (ProgramsUsed+
                    ProgramsUsedInfo01+
                    ProgramsUsedInfo02+
                    ProgramsUsedInfo03)

    # holds the information about how the program works in a array so it can grab them more easily
    info = (HowToUse+
            HowToUseInfo01 +
            HowToUseInfo02 + 
            HowToUseInfo03 + 
            HowToUseInfo04 +
            HowToUseInfo05 +
            HowToUseInfo06 +
            HowToUseInfo07 +
            HowToUseInfo08 +
            HowToUseInfo09 +
            HowToUseInfo10) 

    lineArt(["figlet", "Mac"])
    lineArt(["figlet", "? HELP ?"])
    print(NameOfOs, file=HelpFile)
    print(HELP_LOGO, file=HelpFile)
    
    #inputs the program used logo in a help file
    #puts the info about the program inside the help file
    print(ProgramsUSED)

    #Puts the info logo in the help file
    print(ProgramsUSED, file=HelpFile)

    #puts the info about how to use the program inside the help file
    print(info, file=HelpFile)

    #puts the info about how to use the program on the screen
    print(info)
    
#puts program in GUI mode
def Show_GUI():
    # gets the current time and formats it HH:MM:SS
    current_time = datetime.datetime.now().time()

    formatted_time = current_time.strftime("%I:%M:%S %p")

    # Get the current date
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")

    def connect(url="https://google.com"):
        try:
            urllib.request.urlopen(url)  # Try to open a connection to the host
            return True  # If successful, return True
        except:
            return False  # If unsuccessful, return False
    connect()
    # Makes sure that the user is connected to the internet    

    if platform.system() == OS:
        #checks if the user is running as root
        if os.geteuid() == ROOT:
            #makes the loading bar visible
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
                    print(f'\rLoading {ProgramName} [{bar}] {percentage} % ', end='', flush=False)
                    
                    time.sleep(delay)  # Pause to control the update rate
            print_loading_bar(50)
            subprocess.run(GuiScript)  # the script to run after loading
        else:    
            # makes a pop up dialog to tell the user that the user is not root
            print(f"[ {RED}FAIL{RESET} ] TIME:{formatted_time} Please run as ROOT. DATE:{current_date}")
            print(f"ERROR:TIME:{formatted_time} Please run as ROOT. DATE:{current_date}", file=ERROR)
    else:
        # makes a pop up dialog to tell the user that the OS is not correct
        # makes a pop up dialog to tell the user that the OS is not correct
        print(f"TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}")
        print(f"WARNING:TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}",file=ERROR)

# puts it in GLOBAL mode
def show_GLOBAL():
    # gets the current time and formats it HH:MM:SS
    current_time = datetime.datetime.now().time()

    formatted_time = current_time.strftime("%I:%M:%S %p")

    # Get the current date
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")

    def connect(url="https://google.com"):
        try:
            urllib.request.urlopen(url)  # Try to open a connection to the host
            return True  # If successful, return True
        except:
            return False  # If unsuccessful, return False

    # Makes sure that the user is connected to the internet    

    if platform.system() == OS:
        #checks if the user is running as root
        if os.geteuid() == ROOT:
            #makes the loading bar visible
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
                    print(f'\rLoading {ProgramName} Globally [{bar}] {percentage} % ', end='', flush=False)
                    
                    time.sleep(delay)  # Pause to control the update rate
            print_loading_bar(50)
            subprocess.run(GlobalScript)  # the script to run after loading
        else:    
            # makes a pop up dialog to tell the user that the user is not root
            print(f"[ {RED}FAIL{RESET} ] TIME:{formatted_time} Please run as ROOT. DATE:{current_date}")
            print(f"ERROR:TIME:{formatted_time} Please run as ROOT. DATE:{current_date}", file=ERROR)
    else:
        # makes a pop up dialog to tell the user that the OS is not correct
        # makes a pop up dialog to tell the user that the OS is not correct
        print(f"TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}")
        print(f"WARNING:TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}",file=ERROR)

# puts the program in LOCAL mode
def show_LOCAL():
    # gets the current time and formats it HH:MM:SS
    current_time = datetime.datetime.now().time()

    formatted_time = current_time.strftime("%I:%M:%S %p")

    # Get the current date
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")

    def connect(url="https://google.com"):
        try:
            urllib.request.urlopen(url)  # Try to open a connection to the host
            return True  # If successful, return True
        except:
            return False  # If unsuccessful, return False

    # Makes sure that the user is connected to the internet    
    if platform.system() == OS:
        #makes the loading bar visible
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
                print(f'\rLoading {ProgramName} Locally [{bar}] {percentage} % ', end='', flush=False)
                
                time.sleep(delay)  # Pause to control the update rate
        print_loading_bar(50)
        print(f"\n[ {GREEN}OK{RESET} ] Loading {ProgramName} complete")
        time.sleep(5)
        subprocess.run(LocalScript)  # the script to run after loading
    else:
        # makes a pop up dialog to tell the user that the OS is not correct
        # makes a pop up dialog to tell the user that the OS is not correct
        print(f"TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}")
        print(f"WARNING:TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}",file=ERROR)

#puts the program into GUI LOCAL mode
def show_GuiLOCAL():
    # gets the current time and formats it HH:MM:SS
    current_time = datetime.datetime.now().time()

    formatted_time = current_time.strftime("%I:%M:%S %p")

    # Get the current date
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")

    def connect(url="https://google.com"):
        try:
            urllib.request.urlopen(url)  # Try to open a connection to the host
            return True  # If successful, return True
        except:
            return False  # If unsuccessful, return False

    # Makes sure that the user is connected to the internet    
    if platform.system() == OS:
        #makes the loading bar visible
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
                print(f'\rLoading {ProgramName} Locally [{bar}] {percentage} % ', end='', flush=False)
                
                time.sleep(delay)  # Pause to control the update rate
        print_loading_bar(50)
        subprocess.run(GuiLocalScript)  # the script to run after loading
    else:
        # makes a pop up dialog to tell the user that the OS is not correct
        # makes a pop up dialog to tell the user that the OS is not correct
        print(f"TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}")
        print(f"WARNING:TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}",file=ERROR)

#holds the if statements that connect to the functions for the program to work properly
try:
    # Handle command-line arguments
    #connect to the HELP function of the Hercules program so the user understands what the program does
    if len(sys.argv) == 2 and sys.argv[1] in HELP:
        show_help()
        
    #puts the program into gui mode
    elif len(sys.argv) == 2 and sys.argv[1] in GUI:
        #checks if the user is connected to ssh and if they are it says to disconnected from ssh for the GUI script to work correctly
        #else if they are not connected to ssh it will work normally
        def is_ssh_connection():
            return "SSH_TTY" in os.environ

        if is_ssh_connection() == True:
            print("Connected via SSH. This script will not run.",
                  "Until you disconnect from SSH.")
        else:
            Show_GUI()
    
    #connect to the global function of the Hercules program
    elif len(sys.argv) == 2 and sys.argv[1] in GLOBAL:
        show_GLOBAL()

    #connect to the local function of the Hercules program
    elif len(sys.argv) == 2 and sys.argv[1] in LOCAL:
        show_LOCAL()
    
    #connect to the GuiLocal function of the Hercules program
    elif len(sys.argv) == 2 and sys.argv[1] in GuiLocal:
        show_GuiLOCAL()

    #installs the required packages for the program to work properly
    elif len(sys.argv) == 2 and sys.argv[1] in installRequirement:
        subprocess.run('bash requirements.sh')
    
    #uninstall the required packages so its easier to uninstall them
    elif len(sys.argv) == 2 and sys.argv[1] in uninstallRequirement:
        subprocess.run('bash uninstall.sh')

    #if the user does not input the correct argument it tells them what arguments to use for it to work 
    else:
        print(f"WARNING:TIME:{formatted_time} Please use the correct number of arguments. DATE:{current_date}",file=ERROR)
        print(f"Please use the correct number of arguments.")
        print(f'''Example: 
{GLOBAL} put's it in global mode for attacking global networks, 
{GUI} put's it in GUI mode to attacking in GUI GLOBAL networks, 
{LOCAL} put's it in local mode for attacking local networks,
{GuiLocal} put's it in GUI LOCAL mode to attacking in GUI LOCAL networks,
{installRequirement} put's it in install mode that install's the required packages,
{uninstallRequirement} put's it in uninstall mode that uninstall's the packages,
{HELP} put's it in help mode so you understand what you are going to do with this program.''')

except KeyboardInterrupt:
    print("\n[-] Exiting...")