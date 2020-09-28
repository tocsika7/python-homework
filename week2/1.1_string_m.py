#!/usr/bin/env python3
import sys

# A metódus kicseréli a megadott string karaktereiben az o betűket 😮-ra 

def replace_os(s):
    print(s.replace('o','😮'))

def main():
    replace_os(sys.argv[1])

##############################################################################

if __name__ == "__main__":
    main()