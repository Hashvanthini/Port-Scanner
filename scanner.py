import socket
import time

target = input("Enter the target IP address: ")
print(f"Scanning {target}...")
time.sleep(1)
for port in range(1, 65536):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Set a timeout for the connection attempt
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")

    sock.close()