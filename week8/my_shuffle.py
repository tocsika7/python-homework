from random import shuffle

def my_shuffle(li):
    li2 = li[::]
    shuffle(li2)
    return li2
    

def main():
    li = [12, 27, 35, 16,4]
    print(my_shuffle(li))
    print(my_shuffle(li)[1:2])
    print(li)

if __name__ == "__main__":
    main()