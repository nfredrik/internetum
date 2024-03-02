import contextlib
import os
import socket

import requests
from behave import given, when, then
from ping3 import ping

from features.helper import get_router_ip, get_mac_address, get_ip_address, find_vendor


# https://scapy.readthedocs.io/en/latest/usage.html#tcp-ping


# TODO: Kolla om MAC-addr 6-ställigt?
# går att göra på annat sätt än popen?
# kolla vilken leverantör på MAC-addr ...

@given('my computer has a MAC address')
def step_given_mac_address(context):
    # Implementera steg för att hämta MAC-adressen från datorn
    #context.mac_address = os.popen('ifconfig en0 | awk "/ether/{print $2}"').read().strip()
    #print(f'{context.mac_address=}')
    #assert context.mac_address is not None

    mac_addr:str = get_mac_address()
    print(f'{mac_addr=}')
    x = find_vendor(mac_address=mac_addr)
    print(x)

# Är det en giltigt ipaddr?
@when('I check for an IP address')
def step_when_check_ip_address(context):
    # Implementera steg för att kontrollera om datorn har en giltig IP-adress
    #context.ip_address = os.popen('ifconfig en0 | grep "inet " | awk \'{print $2}\'').read().strip()
    #print(f'{context.ip_address =}')

    ipaddr = get_ip_address()
    print(f'{ipaddr=}')
    assert ipaddr is not None,'Error, invalid ip addr'


@when('I perform a DNS lookup for "{domain}"')
def step_when_dns_lookup(context, domain):
    # Implementera steg för att göra en DNS-slagning
    try:
        context.dns_result = socket.gethostbyname(domain)
    except socket.gaierror:
        context.dns_result = None

    assert context.dns_result is not None
    print(f'{context.dns_result=}')




@then('I should receive a valid DNS response')
def step_then_valid_dns_response(context):
    # Implementera steg för att verifiera en giltig DNS-svar
    assert context.dns_result != ''


@when('I check the nearest router')
def step_when_check_nearest_router(context):
    context.router_response = os.popen("traceroute google.com | grep -m 1 -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | awk 'NR==1 {print}'")
    assert context.router_response is not None

    print(f'{context.router_response=}')

    print(f'{ get_router_ip()=}')

    with contextlib.suppress(requests.ConnectionError):
        context.router_response = requests.get("http://google.com", timeout=5)

@then('I should receive a successful response')
def step_then_successful_response(context):
    # Implementera steg för att verifiera att förfrågan lyckades (statuskod 200)
    assert context.router_response is not None
    assert context.router_response.status_code == 200


@when('I ping "{host}"')
def step_when_ping_host(context, host):
    try:
        # Run the ping command
        #result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, timeout=10)
        context.ping_result = ping(host, timeout=2) is not None


        # Check if the ping was successful (exit code 0)
        #context.ping_result = result.returncode == 0
    except Exception as e:
        print(f"Error during ping: {e}")
        context.ping_result = False


@then('I should receive a successful ping response')
def step_then_successful_ping_response(context):
    assert context.ping_result is not None
    assert context.ping_result is True