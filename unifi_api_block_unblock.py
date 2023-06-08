import os
import requests
import tempfile
import json
import urllib3
import time
import random

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Define the environment variables
username = os.getenv('username', 'ubnt') # replace to your username
password = os.getenv('password', 'ubnt') # replace to your password
baseurl = os.getenv('baseurl', 'https://unifi:8443') #replace to unifi controller ip
site = os.getenv('site', 'default') # replace default with your site name

# Create a temporary file for storing the authentication cookie
cookie = tempfile.NamedTemporaryFile().name

# Set the requests session
session = requests.Session()
session.verify = False

def unifi_requires():
    if not all([username, password, baseurl, site]):
        print("Error! Please define required environment variables.")
        print("Example:")
        print("export username=ubnt")
        print("export password=ubnt")
        print("export baseurl=https://localhost:8443")
        print("export site=default")
        return False
    return True

def unifi_login():
    # Authenticate against the UniFi controller
    login_data = {
        "username": username,
        "password": password
    }
    response = session.post(f'{baseurl}/api/login', json=login_data, verify=False)
    response.raise_for_status()

def unifi_logout():
    # Logout from the UniFi controller
    session.get(f'{baseurl}/logout', verify=False)

def unifi_api(uri, json_data=None):
    # Make an API request to the UniFi controller
    uri = f'/{uri.lstrip("/")}'
    data = json_data or {}
    response = session.post(f'{baseurl}/api/s/{site}{uri}', json=data, verify=False)
    response.raise_for_status()

def unifi_block_sta(mac):
    payload = {
        "cmd": "block-sta",
        "mac": mac
    }
    unifi_api(f'cmd/stamgr', payload)

def unifi_unblock_sta(mac):
    payload = {
        "cmd": "unblock-sta",
        "mac": mac
    }
    unifi_api(f'cmd/stamgr', payload)

# Check if the required environment variables are defined
if unifi_requires():
    # Perform desired operations
    unifi_login()
    
    while True:
        # Wait for a certain interval before blocking the devices
        interval_time = random.randint(1, 5)  # Specify the interval time in seconds
        print(f"Waiting for {interval_time * 60} seconds before blocking...")
        time.sleep(interval_time * 60)
        
        # Block devices by MAC address
        mac_addresses = ["00:00:00:00:00:00","00:00:00:00:00:00"]  # Replace with actual MAC addresses
        for mac in mac_addresses:
            unifi_block_sta(mac)
        
        # Wait for a certain interval before unblocking the devices
        interval_time = random.randint(1, 5)  # Specify the interval time in seconds
        print(f"Waiting for {interval_time * 60} seconds before unblocking...")
        time.sleep(interval_time * 60)
    
        # Unblock devices by MAC address
        for mac in mac_addresses:
            unifi_unblock_sta(mac)
    
    # Logout from the UniFi controller
    unifi_logout()
