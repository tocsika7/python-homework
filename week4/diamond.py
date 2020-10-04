def diamond(h):
    if h % 2 == 0:
        print('Invalid height')
        return 0 

    li = [i for i in range(1,(h+1)//2)]
    li2 = [i for i in reversed(range(1,(h+1)//2))]
    
    for i in li:
        if i == 1:
            print('*'.center(h))
        else:
            print(('*' * (i+(i-1))).center(h))
    
    for i in li2:
        if i == 1:
            print('*'.center(h))
        else:
            print(('*' * (i+(i-1))).center(h))





def main():
    diamond(7)

if __name__ == "__main__":
    main()