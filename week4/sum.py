def main():
    li = [i for i in range(0,1000) if i % 5 == 0 or i % 3 == 0]
    print(sum(li))

if __name__ == "__main__":
    main()