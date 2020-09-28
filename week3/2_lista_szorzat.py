#!/usr/bin/env python3
# encoding: utf-8

def product(li):
    product = 1 
    for i in li:
        product *= i
    return product

def main():
    print(product([4,6,7,8]))



##############################################################################

if __name__ == "__main__":
    main()