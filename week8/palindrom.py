def isPalindrom(num):
    numBinary = bin(num)
    if str(num) == str(num)[::-1] and numBinary[2:] == numBinary[::-1][:-2]:
        return True
    else:
        return False


def main():
    palindroms = []
    for num in range(0,1000000+1):
        if isPalindrom(num):
            palindroms.append(num)

    print(sum(palindroms)) 


if __name__ == "__main__":
    main()
