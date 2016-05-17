# encoding: utf-8


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
