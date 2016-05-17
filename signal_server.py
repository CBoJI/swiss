# encoding: utf-8

from socket import socket, AF_INET, SOCK_DGRAM
import network
from config import SIGNAL_SERVER_PORT

if __name__ == '__main__':
    print 'Start on %s port' % SIGNAL_SERVER_PORT

    udp_socket = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM uses for UDP
    udp_socket.bind(('', SIGNAL_SERVER_PORT))

    network.signal_server(udp_socket)
