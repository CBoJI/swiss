# encoding: utf-8

import sys
import json
import socket

import network

from config import SIGNAL_SERVER_IP, SIGNAL_SERVER_PORT, SERVER_PORT


if __name__ == '__main__':
    print 'Start on %s' % SERVER_PORT

    # socket.setdefaulttimeout(2)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM uses for UDP
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind(('', SERVER_PORT))

    result = network.publish_public_address(s=udp_socket, host=SIGNAL_SERVER_IP, port=SIGNAL_SERVER_PORT, server=True)
    result = json.loads(result)
    if 'error' in result:
        sys.exit(1)

    network.server(udp_socket)
