# Simple-Network-Port-Scanner
Port Scanner Tool – Quick Overview
This is a simple yet effective port scanner designed to check the most commonly used ports on a given IPv4 address. Once the scan is complete, users have the option to save the results as a text file for future reference.

How it works:

Enter the target IPv4 address and press Enter.

Input a name for the results file (use only letters, numbers, and underscores).

The scan will begin and display open or closed ports in real-time.

Platform Compatibility:
This tool can be run on desktop or mobile devices using Python.

Enjoy a quick and easy way to assess network security with just a few keystrokes!

# Ports Included In Scanner:
20,   # FTP (Data)
21,   # FTP (Control)
22,   # SSH
23,   # Telnet
25,   # SMTP
53,   # DNS
67,   # DHCP (Server)
68,   # DHCP (Client)
80,   # HTTP
110,  # POP3
123,  # NTP
135,  # RPC
139,  # NetBIOS
143,  # IMAP
161,  # SNMP
162,  # SNMP Trap
389,  # LDAP
443,  # HTTPS
445,  # SMB
465,  # SMTPS
514,  # Syslog
587,  # SMTP (Submission)
993,  # IMAPS
995,  # POP3S
1433, # Microsoft SQL Server
1521, # Oracle DB
3306, # MySQL
3389, # RDP
5432, # PostgreSQL
5900, # VNC
8080, # HTTP Proxy / Alternative Web
8888  # Jupyter Notebook / Dev Server 

#To open the file automatically on Windows, replace Line 93 line with:
os.system("notepad {output_file}")
If line is not added it will still save in your notepad, it just will not automatically open.
