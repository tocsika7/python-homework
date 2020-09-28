#!/usr/bin/env python3

def is_pallindrome(s):
    if(s == s[::-1]):
        return True
    else:
        return False 

def is_pallindrome_stack(s):
    r = ''
    stack = []
    for i in s: 
        stack.append(i)
    
    while((len(stack)!= 0)):
        r += str(stack.pop())

    if(r == s):
        return True
    else:
        return False

def is_pallindrome_rec(s):
    if len(s) <= 1:
        return True
    else:
        if(s[0] != s[len(s)-1]):
            return False
        else:
            return is_pallindrome_rec(s[1:(len(s)-1)])


def main():
    print(is_pallindrome('indulagörögaludni'))
    print(is_pallindrome_stack('indulagörögaludni'))
    print(is_pallindrome_rec('indulagörögaludni'))

##############################################################################

if __name__ == "__main__":
    main()