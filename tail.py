#
#  Linux tail
#
#
#

import time


def tail(filed):
    print "Started tailing ..."
    filed.seek(0, 2)
    while True:
        _line = filed.readline()
        if not _line:
            time.sleep(0.1)
            continue
        yield _line


if __name__ == "__main__":
    print "Started ... "
    filedesc = open("/var/log/apache2/access.log")
    for line in tail(filedesc):
        print line,

