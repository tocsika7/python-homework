#!/usr/bin/env python3
# encoding: utf-8


def main():
    li = []
    i = 1
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            li.append(i)
    
    print(sum(li))

##############################################################################

if __name__ == "__main__":
    main()