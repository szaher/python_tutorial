#!/usr/bin/env python
#
#
#
#
#
##


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

if __name__ == "__main__":
    test_iterator()
    test_iterator2()
