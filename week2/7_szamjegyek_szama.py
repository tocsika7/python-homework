#!/usr/bin/env python3


def count_digits(n,power):
    p = n**power
    return len(str(p))


def main():
    print(count_digits(2,256))

##############################################################################

if __name__ == "__main__":
    main()