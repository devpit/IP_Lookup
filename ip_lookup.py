import requests
import argparse
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def lookup_ip(ip):
    # API URL from IPinfo with the given IP
    url = f"https://ipinfo.io/{ip}/json"
    
    try:
        # Make the GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Unable to fetch IP data"}
    except Exception as e:
        return {"error": str(e)}

def format_data(data):
    if "error" in data:
        return data["error"]
    
    # Format the data for display
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
        f"{Fore.WHITE}Usage of the IP lookup script:{Style.RESET_ALL}\n\n"
        f"{Fore.YELLOW}python ip_lookup.py -ip IP_ADDRESS{Style.RESET_ALL}\n\n"
        f"{Fore.WHITE}Parameters:{Style.RESET_ALL}\n"
        f"  {Fore.CYAN}-ip, --ipaddress{Style.RESET_ALL}  IP address for lookup\n"
        f"  {Fore.CYAN}-h, --help{Style.RESET_ALL}        Show this help message and exit\n\n"
        f"{Fore.WHITE}Usage examples:{Style.RESET_ALL}\n"
        f"  {Fore.YELLOW}python ip_lookup.py -ip 8.8.8.8{Style.RESET_ALL}\n"
    )
    print(help_text)

def main():
    parser = argparse.ArgumentParser(
        description="Lookup information for an IP address.",
        add_help=False  # Disable the default argparse help message
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
    
    ip = args.ipaddress
    ip_data = lookup_ip(ip)
    formatted_data = format_data(ip_data)
    print(formatted_data)
    
    while True:
        next_step = input(f"\n{Fore.WHITE}Enter a new IP to lookup or type 'exit' to quit:{Style.RESET_ALL} ").strip()
        if next_step.lower() == 'exit':
            print(f"{Fore.YELLOW}Exiting...{Style.RESET_ALL}")
            break
        elif next_step:
            ip_data = lookup_ip(next_step)
            formatted_data = format_data(ip_data)
            print(formatted_data)

if __name__ == "__main__":
    main()
