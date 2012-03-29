# -*- coding: utf-8 -*-

from pgbouncerlib.server import BouncerServer
import logging
import getopt
import sys

def usage():
    print """Make your postgres fly with twhis awesome pice of code!
    
python pgbouncer-ng.py [ARGS]

ARGS:
-h: help
-n --no-log: disables debug info
"""

if __name__ == '__main__':
    
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

    try:                        
        opts, args = getopt.getopt(sys.argv[1:], "hn", ["help", "no-log"]) 
    except getopt.GetoptError:
        print
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-n", "--no-log"):
            logging.disable(logging.DEBUG)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()

    server = BouncerServer()
    server.serve_forever()
