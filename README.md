# IP Lookup 

A Python script to fetch and display information about an IP address using the IPinfo API. This script includes formatted output and user interaction for multiple IP lookups. It leverages the `requests`, `argparse`, and `colorama` libraries for HTTP requests, command-line argument parsing, and colored terminal output, respectively.

## Features

- Fetches data from the IPinfo API
- Formats and displays IP address information
- Supports multiple IP lookups in a single session
- Provides colored terminal output for better readability

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/devpit/IP_Lookup.git
   cd /IP_Lookup
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script with an IP address to lookup:
```sh
python ip_lookup.py -ip 8.8.8.8
```

You can also display the help message:
```sh
python ip_lookup.py -h
```

## Example Output

```plaintext
IP: 8.8.8.8
City: Mountain View
Region: California
Country: US
Location: 37.3860,-122.0840
Organization: AS15169 Google LLC
Postal: 94035
Timezone: America/Los_Angeles
```

After the initial lookup, you can enter additional IP addresses or type `exit` to quit the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
