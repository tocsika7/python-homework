def main():
    li1 = [i*i for i in range(1,100+1)]
    li2 = [i for i in range(1,100+1)]
    negyzetOsszeg = sum(li1)
    osszegNegyzet = pow(sum(li2),2)

    print(osszegNegyzet-negyzetOsszeg)


if __name__ == "__main__":
    main()