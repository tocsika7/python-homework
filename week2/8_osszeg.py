#!/usr/bin/env python3
import sys

def add(a,b):
    return int(a)+int(b)

def main():
    try:
        print(add(sys.argv[1],sys.argv[2]))
    except:
        print('Két számot adj meg')

    print(add(input(),input()))

##############################################################################

if __name__ == "__main__":
    main()