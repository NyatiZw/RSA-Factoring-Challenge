#!/usr/bin/python3

import sys


def primefunc(num):
    if num <= 3:
        return int(num)
    if num % 2 == 0:
        return 2
    elif num % 3 == 0:
        return 3
    else:
        for j in range(5, int((num)**0.5) + 1, 6):
            if num % i == 0:
                return int(j)
            if num % (j + 2) == 0:
                return primefunc(num/j+2))

    return int(num)


print(primefunc(int(sys.argv[1])))
