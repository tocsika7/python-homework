#!/usr/bin/env python

import sys


''' Függvény amely kiírja az angol abc kisbetűit. 
@param reverse : bool Igaz érték esetén fordítva írja ki az abc betűit.'''
def printABC(reverse=False):
    abc = ''
    for i in range(97,122):
        abc += chr(i)

    if reverse:
        print(abc[::-1])
    else:
        print(abc)



def main():
    if sys.argv[0] == './a-z.py':
        printABC()
    elif sys.argv[0] == './z-a.py':
        printABC(True)   


if __name__ == "__main__":
    main()