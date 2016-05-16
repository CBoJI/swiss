# encoding: utf-8

from socket import socket, AF_INET, SOCK_DGRAM

import network
from config import SERVER_ADDRESS, SIGNAL_SERVER_ADDRESS

if __name__ == '__main__':
    print 'Start on %s %s' % SERVER_ADDRESS

    udp_socket = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM uses for UDP
    udp_socket.bind(SERVER_ADDRESS)

    network.publish_public_address(*SIGNAL_SERVER_ADDRESS, server=True)

    network.server(udp_socket)
