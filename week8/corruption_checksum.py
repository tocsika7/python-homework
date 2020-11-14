def main():
    with open('input.txt','r') as input:
        kulonbsegek = []
        for line in input:
            line = line.rstrip('\n')
            maxValue = max([int(i) for i in line.split()])
            minValue = min([int(i) for i in line.split()])
            kulonbsegek.append(maxValue-minValue)
        
        print(sum(kulonbsegek))

if __name__ == "__main__":
    main()