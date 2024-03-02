import re
import socket
import subprocess
import uuid

import netifaces
import requests
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp


def get_router_ip():
    gateways = netifaces.gateways()
    return gateways['default'][netifaces.AF_INET][0]


def get_mac_address() -> str:
    return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xFF) for elements in range(0, 2 * 6, 2)][::-1])


def get_arp_table():
    arp = ARP(pdst='192.168.1.0/24')
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    return [{'ip': received.psrc, 'mac': received.hwsrc} for sent, received in result]


def get_ip_address() -> str:
    try:
        # Create a socket connection to a remote host (in this case, Google's public DNS server)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
    except socket.error as e:
        print(f"Error getting IP address: {e}")
        ip_address = None
    finally:
        s.close()

    return ip_address


def find_vendor(mac_address) -> str | None:
    api_url = f'https://api.macvendorlookup.com/{mac_address}/json'

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200 and data['result'] == 'found':
            return data['vendor']
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_first_router() -> str | None:
    try:
        # Run traceroute command and capture the output
        result = subprocess.run(['traceroute', 'google.com'], capture_output=True, text=True)

        if match := re.search(r'\((\d+\.\d+\.\d+\.\d+)\)', result.stdout):
            return match[1]
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None
