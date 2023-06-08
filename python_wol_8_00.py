import socket
import binascii
import struct
import re
import datetime
import time

MAC = "00:00:00:00:00:00" #replace current Mac

def format_mac(mac):
    mac_re = re.compile(r'''
                      (^([0-9A-F]{1,2}[-]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[:]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[.]){5}([0-9A-F]{1,2})$
                      )''', re.VERBOSE | re.IGNORECASE)

    if re.match(mac_re, mac):
        if mac.count(':') == 5 or mac.count('-') == 5 or mac.count('.'):
            sep = mac[2]
            mac_fm = mac.replace(sep, '')
            return mac_fm
    else:
        raise ValueError('Incorrect MAC format')

def create_magic_packet(mac):
    data = b'FF' * 6 + (mac * 16).encode()
    send_data = b''
    for i in range(0, len(data), 2):
        send_data = send_data + struct.pack('B', int(data[i: i + 2], 16))
    return send_data

def send_magic_packet(send_data):
    broadcast_address = '255.255.255.255'
    port = 9
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(send_data, (broadcast_address, port))
    s.close()

def is_weekday():
    now = datetime.datetime.now()
    return now.weekday() < 5  # Monday to Friday is considered a weekday (0-4)

def is_wakeup_time():
    now = datetime.datetime.now()
    return now.weekday() < 5 and now.hour == 7 and now.minute == 55

if __name__ == '__main__':
    mac = format_mac(MAC)

    while True:
        if is_wakeup_time():
            send_data = create_magic_packet(mac)
            send_magic_packet(send_data)
            print("Magic Wake-Up packet sent!")
        
        # Sleep for 1 minute before checking the conditions again
        time.sleep(60)
