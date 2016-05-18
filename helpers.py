# encoding: utf-8

import stun


def stoppable(func):
    """ break by ctrl+c """
    def wrapper(s):
        print '-' * 80
        print 'Press Ctrl+C to stop.'
        try:
            func(s)
        except KeyboardInterrupt:
            print 'bye'
            import sys
            sys.exit(0)

    return wrapper


def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)


def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')


def get_ip_info_by_socket(s, source_ip="0.0.0.0", source_port=54320, stun_host=None, stun_port=3478):
    """ Override function from pystun module. No need to create new socket. """

    nat_type, nat = stun.get_nat_type(s, source_ip, source_port,
                                 stun_host=stun_host, stun_port=stun_port)

    external_ip = nat['ExternalIP']
    external_port = nat['ExternalPort']

    return (nat_type, external_ip, external_port)
