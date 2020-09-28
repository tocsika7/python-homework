import string

def main():
    i = 0 
    li = []
    for i in range(33,127):
        print('{0}: {1}'.format(i,chr(i))) 
        if  chr(i) in string.ascii_uppercase:
            li.append(i)

    print(sum(li))



if __name__ == "__main__":
    main()

    