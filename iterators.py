#!/usr/bin/env python
#
#
#
#
#
##
import itertools


def test_iterator():
    """Test reading from file as iterator example"""
    filed = open("/tmp/saad/x")
    # first argument to iter should be callable function, second line should be
    #  what is going to stop the iterator. for example if you reach this line
    #  you should stop and return. leaving it empty means when you hit the end
    #  of the file
    for line in iter(filed.readline, ""):
        print line


def test_iterator2():
    """Use list collection to build an iterator"""
    a = [1, 2, 3, 4, 10, 12, 15, 17]
    x = iter(a)
    while True:
        try:
            print x.next()
        except StopIteration:
            break


class MString(object):
    def __init__(self, istr):
        self.index = 0
        self.istr = istr

    def __next__(self):
        return self.next()

    def next(self):
        try:
            char = self.istr[self.index]
            self.index += 1
            return char
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


def test_mstring():
    string = "Python is Great"
    myiter = MString(istr=string)
    for i in myiter:
        print i,
    print ""


# drop me


def dropme(x):
    if x < 10:
        return True
    else:
        return False


def test_drop():
    droplet = itertools.dropwhile(dropme, sorted([1, 3, 4, 1, 66, 1, 5, 7, 8, 3, 2]))
    for d in droplet:
        print d


if __name__ == "__main__":
    test_iterator()
    test_iterator2()
    test_mstring()
    test_drop()

