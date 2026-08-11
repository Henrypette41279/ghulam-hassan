"""
Subnet Calculator
A simple CLI tool to calculate network details from an IP address and subnet mask.
Built to demonstrate CCNA / networking fundamentals.

Author: Ghulam Hassan
"""

import ipaddress


def calculate_subnet(ip_with_cidr: str):
    try:
        network = ipaddress.ip_network(ip_with_cidr, strict=False)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    print("\n--- Subnet Details ---")
    print(f"Network Address     : {network.network_address}")
    print(f"Broadcast Address   : {network.broadcast_address}")
    print(f"Subnet Mask         : {network.netmask}")
    print(f"Wildcard Mask       : {network.hostmask}")
    print(f"CIDR Notation       : /{network.prefixlen}")
    print(f"Total Addresses     : {network.num_addresses}")
    usable = list(network.hosts())
    print(f"Usable Hosts        : {len(usable)}")
    if usable:
        print(f"First Usable Host   : {usable[0]}")
        print(f"Last Usable Host    : {usable[-1]}")
    print(f"Is Private Range    : {network.is_private}")
    print("-----------------------\n")


def main():
    print("=== Subnet Calculator ===")
    print("Enter an IP address with CIDR notation (e.g., 192.168.1.0/24)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter IP/CIDR: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        calculate_subnet(user_input)


if __name__ == "__main__":
    main()
