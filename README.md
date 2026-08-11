"""
Subnet Calculator
A simple CLI tool to calculate network details from an IP address and subnet mask.
Built to demonstrate CCNA / networking fundamentals.

Author: Ghulam Hassan
"""


if __name__ == "__main__":
    main()# ghulam-hassan
    🌐 Subnet Calculator
A simple Python CLI tool that calculates subnet details (network address, broadcast address, usable host range, etc.) from an IP address and CIDR notation.
Built to apply networking fundamentals learned through CCNA certification.
💡 Features
	•	Calculates network & broadcast address
	•	Shows subnet mask and wildcard mask
	•	Lists usable host range
	•	Detects private vs public IP ranges
	•	Simple interactive command-line interface
🚀 How to Run
python subnet_calculator.py
Then enter an IP with CIDR, for example:
192.168.1.0/24
📷 Example Outpu
Enter IP/CIDR: 192.168.1.0/24

--- Subnet Details ---
Network Address     : 192.168.1.0
Broadcast Address   : 192.168.1.255
Subnet Mask         : 255.255.255.0
Wildcard Mask       : 0.0.0.255
CIDR Notation       : /24
Total Addresses     : 256
Usable Hosts        : 254
First Usable Host   : 192.168.1.1
Last Usable Host    : 192.168.1.254
Is Private Range    : True
-----------------------
🛠️ Tech Used
	•	Python 3 (built-in ipaddress module — no external dependencies)
👤 Author
Ghulam Hassan — CCNA Certified | IT Professional
