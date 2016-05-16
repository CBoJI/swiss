# encoding: utf-8

import sys
from socket import socket, AF_INET, SOCK_DGRAM
import json

import network
from config import SIGNAL_SERVER_ADDRESS
from helpers import safe_str, safe_unicode


if __name__ == '__main__':
    data = network.publish_public_address(*SIGNAL_SERVER_ADDRESS)
    data = json.loads(data)
    server_address = (data['server']['ip'], data['server']['port'])
    udp_socket = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM uses for UDP

    data = raw_input('write to server: ')
    if not data :
        udp_socket.close()
        sys.exit(1)

    data = safe_str(data)
    udp_socket.sendto(data, server_address)

    data = safe_unicode(data)
    data = udp_socket.recvfrom(1024)
    print(data)

    udp_socket.close()
