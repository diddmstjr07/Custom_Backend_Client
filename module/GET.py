import subprocess
subprocess.run(['pip', 'install', 'scapy', '-q'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

from scapy.all import IP, TCP, sr1, ICMP, send, sniff, Raw, ARP, UDP
import subprocess
import os
import re

if os.getuid() != 0:
    print("\033[1m\033[31m" + "[ERROR]" + "\033[0m", "Please start Program as Root (sudo)")
    os._exit(0)

def GET(SRC, DST, SRC_PORT, DST_PORT, DATA):
    mes = Raw(str(DATA))
    ip = IP(src=SRC, dst=DST)
    tcp = UDP(dport=SRC_PORT, sport=DST_PORT)
    packet = ip/tcp/mes
    response = sr1(packet)
    MES = response[Raw].load.decode()
    print("\033[1m\033[92m" + f"{MES}" + "\033[0m")

def INNERIP():
    try:
        result = subprocess.run(['ifconfig'], stdout=subprocess.PIPE, text=True)
        lines = result.stdout.split('\n')
        
        for line in lines:
            ip_address = re.search(r'inet 192\.(\d+\.\d+\.\d+)', line)
            if ip_address:
                ip = ip_address.group(1)
                ip = "192." + str(ip)
        return ip
    except UnboundLocalError:
        print("\033[1m\033[31m" + "[ERROR]" + "\033[0m", "Internet Protocol is not connected")
        os._exit(0)