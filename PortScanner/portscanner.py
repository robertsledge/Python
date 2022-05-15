#!/usr/bin/env python

import socket
import subprocess
import sys
from time import time
import platform

# Screen Clear
subprocess.call('clear' if platform.platform() in ("Linux", "Darwin") else "cls", shell=True)

# Input Prompt
remoteServer = input("Enter a host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Banner
print("-" * 60)
print("Scanning remote host. Please wait...", remoteServerIP)
print("-" * 60)

# Scan start time
t1 = time()

# Specify ports with range variable (Currently 1 - 1024)

# Error handling

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("User Interrupt -  Ctrl+C")
    sys.exit(2)

except socket.gaierror:
    print('Sorry, hostname could not be resolved. Exiting')
    sys.exit(1)

except socket.error:
    print("Couldn't connect to server")
    sys.exit(3)

# Another time check
t2 = time()

# Subtract t2 time start time
total = t2 - t1

# Print results
print('Scan Complete. Time: {total} seconds', total)
