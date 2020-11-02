def main():
    with open('bemenet.txt','r') as f:
        lines = f.read().splitlines()
        count = 0
        for line in lines:
            li = line.split()
            print(li)
            if len(li) == len(set(li)):
                count += 1
        
        print(count)

if __name__ == "__main__":
    main()