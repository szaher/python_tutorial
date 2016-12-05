#!/usr/bin/env python
#
# Inverse generator ( coroutine )
#
#
#


def grep(pattern):
    print "Looking for pattern:", pattern
    while True:
        line = (yield)
        if pattern in line:
            print line,


if __name__ == "__main__":
    g = grep("test")
    # initialize the generator
    g.next()

    # check some data if contains the pattern the generator will print it
    g.send("Hello World !")
    g.send("Welcome to python class")
    g.send("This is just a test !")
    g.send("Test works fine !")
    g.close()


