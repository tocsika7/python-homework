def sumOfDigits(num):
    li = [int(d) for d in str(num)]
    return sum(li)

def main():
    print(sumOfDigits(2 ** 1000))

if __name__ == "__main__":
    main()