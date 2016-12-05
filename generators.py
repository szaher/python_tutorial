#!/usr/bin/env python3
#
# Cool stuff about generators
#
#

from __future__ import print_function
import time
import copy

# Test using return statement at the end of a generator

def countdown(number):
    """Countdown starting from a certain number till 0 then return 0 with are
     turn statement. This works only in python 3"""
    print ("Start counting from", number)
    while number > 0:
        time.sleep(0.2)
        yield number
        number -= 1
    return 10


def test_countdown(number):
    """Try to hit the StopIteration Exception to see what will return"""
    x = countdown(number)
    for i in range(0, number+1):
        try:
            print (next(x))
        except StopIteration as e:
            print (e.value)



# Test delegation of generators

def chain(x, y):
    """Use more than one yield statement in the same generator"""
    yield from x
    yield from y


def test_chain():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    c = copy.copy(a)
    d = copy.copy(b)
    c.reverse()
    d.reverse()
    for i in chain(chain(d, b), chain(a, c)):
        for x in range(0, int(i)):
            print ("*", end="")
        print (" ")

    # for i in chain(chain(chain(a, b), chain(d, c)), chain(chain(chain(a, b), chain(d, c)), chain(chain(a, b), chain(d, c)))):
    #     for x in range(0, int(i)):
    #         print ("*", end="")
    #     print (" ")


# decorator
def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper


def my_coroutine():
    print ("Welcome to my coroute")
    while True:
        line = (yield)
        print (line)


def test_mycoroutine():
    # getting a generator
    mygeni = my_coroutine()
    # initializing the generator
    next(mygeni)
    # send some data to be processed by our generator
    mygeni.send("coroutines are beautiful!")
    mygeni.send("That's really nice !")
    # close it or it will keep consuming memory for ever !
    mygeni.close()



if __name__ == "__main__":
    print ("Hello World !")
#     test_countdown(5)
#     test_chain()
    test_mycoroutine()