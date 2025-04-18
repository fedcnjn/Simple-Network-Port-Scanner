import socket
import time
import random
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init()

# Globals for config
target_ip = ""
port_list = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 1433, 3306, 3389, 8080, 8443, 8888]
stealth_mode = False
output_filename = "scan_results"

def main_menu():
    while True:
        print("\n========== Port Scanner CLI ==========")
        print("1. Set Target IP")
        print("2. Set Port List")
        print("3. Toggle Stealth Mode (Current: " + ("ON" if stealth_mode else "OFF") + ")")
        print("4. Set Output File Name")
        print("5. Run Scan")
        print("6. Exit")
        print("======================================")
        choice = input("Enter your choice: ")

        if choice == "1":
            set_target_ip()
        elif choice == "2":
            set_port_list()
        elif choice == "3":
            toggle_stealth()
        elif choice == "4":
            set_output_name()
        elif choice == "5":
            if target_ip:
                run_scan()
            else:
                print(Fore.RED + "[!] Please set a target IP first!" + Style.RESET_ALL)
        elif choice == "6":
            print("Exiting... Stay dangerous.")
            break
        else:
            print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)

def set_target_ip():
    global target_ip
    target_ip = input("Enter target IP address: ").strip()

def set_port_list():
    global port_list
    print("\nDefault Ports:")
    print(port_list)
    custom = input("Enter custom ports separated by commas (or leave blank to keep default): ").strip()
    if custom:
        try:
            port_list = list(map(int, custom.split(",")))
        except:
            print(Fore.RED + "Invalid input. Keeping default port list." + Style.RESET_ALL)

def toggle_stealth():
    global stealth_mode
    stealth_mode = not stealth_mode
    print("Stealth mode is now", "ON" if stealth_mode else "OFF")

def set_output_name():
    global output_filename
    output_filename = input("Enter output file name (no extension): ").strip()

def run_scan():
    global target_ip, port_list, stealth_mode, output_filename

    output_file = f"{output_filename}.txt"
    open_ports = 0
    closed_ports = 0
    banners_grabbed = 0
    results = []

    if stealth_mode:
        random.shuffle(port_list)
        stealth_delay = 0.5
    else:
        stealth_delay = 0

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results.append(f"Scan Results for {target_ip}")
    results.append(f"Date & Time: {timestamp}\n")

    print(f"\nScanning {target_ip}...\n")
    start_time = time.time()

    for port in port_list:
        try:
            sock = socket.socket()
            sock.settimeout(2)
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                print(Fore.GREEN + f"[+] Port {port} is OPEN" + Style.RESET_ALL)
                results.append(f"[+] Port {port} is OPEN")
                open_ports += 1

                try:
                    sock.sendall(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
                    banner = sock.recv(1024).decode(errors="ignore").strip()
                    if banner:
                        print("    [-] Banner:", banner)
                        results.append(f"    [-] Banner: {banner}")
                        banners_grabbed += 1
                    else:
                        print("    [-] No banner received")
                        results.append("    [-] No banner received")
                except:
                    print("    [-] Failed to grab banner")
                    results.append("    [-] Failed to grab banner")
            else:
                print(Fore.RED + f"[-] Port {port} is CLOSED" + Style.RESET_ALL)
                results.append(f"[-] Port {port} is CLOSED")
                closed_ports += 1

            sock.close()
            time.sleep(stealth_delay)

        except Exception as e:
            print(Fore.RED + f"[!] Error on port {port}: {e}" + Style.RESET_ALL)
            results.append(f"[!] Error on port {port}: {e}")

    end_time = time.time()
    scan_time = round(end_time - start_time, 2)

    # Summary
    results.append("\n--- Scan Summary ---")
    results.append(f"Total Ports Scanned: {len(port_list)}")
    results.append(f"Open Ports: {open_ports}")
    results.append(f"Closed Ports: {closed_ports}")
    results.append(f"Banners Grabbed: {banners_grabbed}")
    results.append(f"Time Taken: {scan_time} seconds")

    with open(output_file, "w") as f:
        for line in results:
            f.write(line + "\n")

    print(Fore.CYAN + f"\n[+] Scan complete. Results saved to {output_file}" + Style.RESET_ALL)

# Start the menu
main_menu()