#!/bin/bash

clear

RED='\033[1;91m'
GREEN='\033[1;92m'
YELLOW='\033[1;93m'
BLUE='\033[1;94m'
MAGENTA='\033[1;95m'
CYAN='\033[1;96m'
WHITE='\033[1;97m'
RESET='\033[0m'

echo
echo -e "${CYAN}$(figlet lpnodes)${RESET}"
echo "A Paid & Free VPS Hosting Company with 600+ Members (discord.gg/lpnodes)"

declare -A SERVERS
SERVERS=(
    [nl-1]="sshx@localhost"
)

PASSWORD="ssh"

echo -e "\n┌──(enter@node)-[~] ${RESET}"
echo -ne "${RED}└─> ${RESET}"
read SERVER_KEY

if [[ -z "${SERVERS[$SERVER_KEY]}" ]]; then
    echo
    echo -e "${RED}Error: Server '$SERVER_KEY' not found!${RESET}"
    echo
    exit 1
fi

USER_HOST=${SERVERS[$SERVER_KEY]}

echo -e "${GREEN}Connecting to $USER_HOST...${RESET}"
sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no "$USER_HOST"
