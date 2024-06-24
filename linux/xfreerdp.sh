#!/bin/bash
source DontEdit.sh
clear
# quits program with ctrl-c
EXIT_PROGRAM_WITH_CTRL_C() {
    echo -e "${RED}[-]${NC} EXITING SOFTWARE..."
    # Add cleanup commands here
    exit 1
}

# quits program with ctrl-z
EXIT_PROGRAM_WITH_CTRL_Z(){
    echo ""
    echo -e "${RED}[-]${NC} EXITING SOFTWARE..."
    # Add cleanup commands here
    exit 1
}

# Function to be executed when Ctrl+Z is pressed
handle_ctrl_z() {
    EXIT_PROGRAM_WITH_CTRL_Z
    exit 1
    # Your custom action goes here
}

# Set up the trap to call the function on SIGTSTP (Ctrl+Z)
trap 'handle_ctrl_z' SIGTSTP

# Function to handle Ctrl+C
ctrl_c() {
    echo ""
    EXIT_PROGRAM_WITH_CTRL_C
}

trap ctrl_c SIGINT

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}
# Function to handle xfreerdp connection
ConnectXfreerdp() {
    if [[ "${OSTYPE}" == "linux-gnu"* ]]; then


        FILE="connections.env"
        figlet -f slant "xfreerdp"

        # Check if file exists
        if [ -e "${FILE}" ]; then
            source "${FILE}"
            xfreerdp /u:"${XFREERDP_USERNAME}" /v:"${XFREERDP_IP}" /p:"${XFREERDP_PASSWORD}"
        else
            sudo nmap -sS 192.168.1.1/24 -Pn -oN scan.txt --open
            echo
            read -p "Input IP: " ip
            read -p "Input username: " username
            read -s -p "Input password: " password
            echo
            read -p "Do you want to save this connection? (y/n) " save
            if [[ "${save}" == "y" ]]; then
                echo "XFREERDP_IP=${ip}" >> "${FILE}"
                echo "XFREERDP_USERNAME=${username}" >> "${FILE}"
                echo XFREERDP_PASSWORD="${password}" >> "${FILE}"
                
                echo "Loading xfreerdp server..."
                sleep 1
                xfreerdp /v:"${ip}" /u:"${username}" /p:"${password}"
            else
                echo
                echo "Loading xfreerdp server..."
                sleep 1
                xfreerdp /u:"${username}" /v:"${ip}" /p:"${password}"
                exit
            fi
        fi
    else
        echo -e "[ ${BRIGHT}${RED}FAIL${NC} ]This script can only be run on Linux"
        exit

    fi
}

# Call the function
ConnectXfreerdp
