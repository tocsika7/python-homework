def isMunchausen(num):
    digit_pows = []
    for c in str(num):
        if c == '0':
            digit_pows.append(0)
        else:
           digit_pows.append(int(c) ** int(c) )
    
    if(sum(digit_pows) == num):
        return True
    else:
        return False
    

def main():
    munchausen_nums = []
    for i in range(0,440000000):
        if isMunchausen(i):
            munchausen_nums.append(i)

    print(munchausen_nums)

if __name__ == "__main__":
    main()