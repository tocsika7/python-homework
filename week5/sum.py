def main():
    digits = ''
    for i in range(1,100+1):
        digits += str(i)

    li = [int(d) for d in list(digits)]
    print(sum(li))
   
if __name__ == "__main__":
    main()