#!/usr/bin/env python
#  Linux tail
#
#
#

import time


def tailf(filed):
    """Python like tail generator. It takes a file descriptor and keeps for
    waiting for data to arrive to the file. """
    print "Started tailing ..."
    # go to the end of the file
    filed.seek(0, 2)
    # keep looping to read from the file
    while True:
        # read some lines
        _line = filed.readline()
        # if there wasn't any new lines wait a little bit and do another loop
        if not _line:
            time.sleep(0.1)
            continue
        # send lines read from the log file

        yield _line


if __name__ == "__main__":
    # open a file and get a file descriptor
    filedesc = open("/var/log/apache2/access.log")
    # read from the generator all newly arrived lines and print them to
    # console.
    for line in tailf(filedesc):
        print line,

