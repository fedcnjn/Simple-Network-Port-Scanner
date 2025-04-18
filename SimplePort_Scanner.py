import socket
from datetime import datetime
import os

target = input("Enter IP address to scan: ")
filename = input("Enter a name for the output file (no extension): ")
output_file = f"{filename}.txt"

common_ports = [
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
]
results = []

# Add timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
results.append(f"Scan Results for {target}")
results.append(f"Date & Time: {timestamp}\n")

print(f"\nScanning {target}...\n")

for port in common_ports:
    try:
        sock = socket.socket()
        sock.settimeout(2)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
            results.append(f"[+] Port {port} is OPEN")

            try:
                sock.sendall(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
                banner = sock.recv(1024).decode(errors="ignore").strip()
                if banner:
                    print(f"    [-] Banner: {banner}")
                    results.append(f"    [-] Banner: {banner}")
                else:
                    print("    [-] No banner received")
                    results.append("    [-] No banner received")
            except:
                print("    [-] Failed to grab banner")
                results.append("    [-] Failed to grab banner")
        else:
            print(f"[-] Port {port} is CLOSED")
            results.append(f"[-] Port {port} is CLOSED")

        sock.close()

    except Exception as e:
        print(f"[!] Error on port {port}: {e}")
        results.append(f"[!] Error on port {port}: {e}")

# Save to file
with open(output_file, "w") as f:
    for line in results:
        f.write(line + "\n")

print(f"\n[+] Results saved to: {output_file}")

# Try to open the file (may vary depending on app)
try:
    os.system(f"open {output_file}")
except:
    print("[*] File saved but could not auto-open. Open it manually in your editor.")