#This script scans LAN to find  devices on port 80
import socket
import ipaddress
import threading

def scan_ip(ip):
    try:
        socket.setdefaulttimeout(1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((str(ip), 80))
        if result == 0:
            print(f"[+] Device found at {ip}")
        sock.close()
    except Exception:
        pass

network = ipaddress.ip_network("192.168.0.0/24", strict=False)
threads = []

for ip in network.hosts():
    t = threading.Thread(target=scan_ip, args=(ip,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

