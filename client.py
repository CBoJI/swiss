# encoding: utf-8

import sys
import json

import network

from config import SIGNAL_SERVER_IP, SIGNAL_SERVER_PORT


if __name__ == '__main__':
    data = network.publish_public_address(host=SIGNAL_SERVER_IP, port=SIGNAL_SERVER_PORT)
    data = json.loads(data)

    if 'error' in data:
        sys.exit(1)

    if data['server']['status'] == 'off':
        print 'server is offline'
        sys.exit(1)

    data = raw_input('write to server: ')
    if not data:
        sys.exit(1)

    network.udp_send(data['server']['ip'], data['server']['port'], data)
