#!/usr/bin/env python3

def hello(s):
    return f'Hello {s.strip()}!'

def main():
    print('Name:')
    print(hello(input()))


##############################################################################

if __name__ == "__main__":
    main()