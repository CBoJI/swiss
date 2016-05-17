# encoding: utf-8

import sys
import socket
import json
from contextlib import closing

import stun

from helpers import stoppable, safe_str, safe_unicode

from config import STUN_HOST


SIGNAL_SERVER_RECORDS = {
    'server': {'ip': '', 'port': '', 'status': 'off'},
    'client': {'ip': '', 'port': '', 'status': 'off'},
}


def publish_public_address(host, port, server=False):
    """
    Get public address by STUN and publish it to the signal server

    :param host: destination host of signal server
    :param port: destination port of signal server
    :param server: specify server or client is published
    """

    print '-' * 80
    print 'Connecting to STUN server'

    nat_type, external_ip, external_port = stun.get_ip_info(stun_host=STUN_HOST)

    print '\tSTUN data:', nat_type, external_ip, external_port

    print '-' * 80
    print 'Publish address to signal server'

    data = {
        'type': 'client',
        'external_ip': external_ip,
        'external_port': external_port
    }
    if server:
        data['type'] = 'server'
    data = json.dumps(data)

    return udp_send(host, port, data)


def udp_send(host, port, data):
    """
    Sends data by UDP to host:port.

    :param host: destination host
    :param port: destination port
    :param data: data to send
    :return: received data
    """

    result = None
    # ensure that socket will be closed
    with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as udp_socket:  # SOCK_DGRAM for UDP
        data = safe_str(data)
        udp_socket.sendto(data, (host, port))

        try:
            data, addr = udp_socket.recvfrom(1024)
        except socket.timeout, e:
            print 'Host not available: %s %s' % (host, port)
            sys.exit(1)

        data = safe_unicode(data)
        result = data
        print '\t%s' % data

    return result


@stoppable
def server(udp_socket):
    """ server logic """

    # ensure that socket will be closed
    with closing(udp_socket) as udp_socket:
        print 'Start listening...'
        while True:
            data, addr = udp_socket.recvfrom(1024)  # receives UPD message and clients address
            print '\tclient connected %s %s' % (addr)
            print '\treceived data:   %s' % data

            udp_socket.sendto(b'message received by the server', addr)  # send msg to client


@stoppable
def signal_server(udp_socket):
    """ signal_server logic """

    # ensure that socket will be closed
    with closing(udp_socket) as udp_socket:
        print 'Start listening...'
        while True:
            data, addr = udp_socket.recvfrom(2048)  # receives UPD message and clients address
            print '\tclient connected %s %s' % (addr)
            print '\treceived data:   %s' % data

            data = safe_unicode(data)
            try:
                data = json.loads(data)
            except ValueError, e:
                print '\tWrong data'
                msg = {'error': 'not json data'}
            else:
                client_type = data['type']
                external_ip = data['external_ip']
                external_port = data['external_port']

                SIGNAL_SERVER_RECORDS[client_type]['ip'] = external_ip
                SIGNAL_SERVER_RECORDS[client_type]['port'] = external_port
                SIGNAL_SERVER_RECORDS[client_type]['status'] = 'on'

                msg = {
                    'status': 'address published',
                }
                if client_type == 'client':
                    msg.update({'server': SIGNAL_SERVER_RECORDS['server']})

            msg = json.dumps(msg)
            msg = safe_str(msg)
            udp_socket.sendto(msg, addr)  # send msg to client
