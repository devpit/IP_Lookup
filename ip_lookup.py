import requests
import argparse
import sys
from colorama import Fore, Style, init
import re
import time
import logging

# Initialize colorama
init(autoreset=True)

# Initialize logging
logging.basicConfig(level=logging.INFO)

def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return bool(pattern.match(ip))

def lookup_ip(session, ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = session.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def format_data(data):
    if "error" in data:
        return data["error"]
    
    formatted_data = (
        f"IP: {data.get('ip', 'Not found')}\n"
        f"City: {data.get('city', 'Not found')}\n"
        f"Region: {data.get('region', 'Not found')}\n"
        f"Country: {data.get('country', 'Not found')}\n"
        f"Location: {data.get('loc', 'Not found')}\n"
        f"Organization: {data.get('org', 'Not found')}\n"
        f"Postal: {data.get('postal', 'Not found')}\n"
        f"Timezone: {data.get('timezone', 'Not found')}\n"
    )
    return formatted_data

def show_help():
    help_text = (
        f"\n"
        f"  {Fore.GREEN}██ ██████      ██       ██████   ██████  ██   ██ ██    ██ ██████  {Style.RESET_ALL}\n"
        f"  {Fore.GREEN}██ ██   ██     ██      ██    ██ ██    ██ ██  ██  ██    ██ ██   ██ {Style.RESET_ALL}\n"
        f"  {Fore.GREEN}██ ██████      ██      ██    ██ ██    ██ █████   ██    ██ ██████  {Style.RESET_ALL}\n"
        f"  {Fore.GREEN}██ ██          ██      ██    ██ ██    ██ ██  ██  ██    ██ ██      {Style.RESET_ALL}\n"
        f"  {Fore.GREEN}██ ██          ███████  ██████   ██████  ██   ██  ██████  ██ {Style.RESET_ALL}\n\n"
        f"  {Fore.WHITE}IP Lookup | Terminal Query - Usage:{Style.RESET_ALL}\n\n"
        f"  {Fore.WHITE}Parameters:{Style.RESET_ALL}\n\n"
        f"  {Fore.CYAN}-ip, --ipaddress{Style.RESET_ALL} IP address for lookup\n"
        f"  {Fore.CYAN}-h, --help{Style.RESET_ALL} Show this help message and exit\n\n"
        f"  {Fore.WHITE}Usage examples:{Style.RESET_ALL}\n\n"
        f"  {Fore.YELLOW}python ip_lookup.py -ip 8.8.8.8{Style.RESET_ALL}\n\n"
        f"  {Fore.WHITE}Credits:{Style.RESET_ALL}\n"
        f"  {Fore.WHITE}Developed by Pit:{Style.RESET_ALL}\n"
        f"  {Fore.WHITE}https://github.com/devpit/IP_Lookup{Style.RESET_ALL}\n"
    )
    print(help_text)

def handle_ip_lookup(session, ip):
    if not is_valid_ip(ip):
        print(Fore.RED + "Invalid IP address format." + Style.RESET_ALL)
        return
    ip_data = lookup_ip(session, ip)
    print(format_data(ip_data))

def main():
    parser = argparse.ArgumentParser(
        description="Lookup information for an IP address.",
        add_help=False
    )
    parser.add_argument("-ip", "--ipaddress", help="IP address for lookup.")
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit")
    
    args = parser.parse_args()
    
    if args.help:
        show_help()
        sys.exit(0)
    
    if not args.ipaddress:
        show_help()
        sys.exit(1)
    
    session = requests.Session()
    handle_ip_lookup(session, args.ipaddress)
    
    while True:
        next_step = input(f"\n{Fore.WHITE}Enter a new IP to lookup or type 'exit' to quit:{Style.RESET_ALL} ").strip()
        if next_step.lower() == 'exit':
            print(f"{Fore.YELLOW}Exiting...{Style.RESET_ALL}")
            break
        elif next_step:
            handle_ip_lookup(session, next_step)
            time.sleep(1)

if __name__ == "__main__":
    main()
