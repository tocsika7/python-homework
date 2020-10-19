def diamond(h):
    height = int(input())
    if height % 2 == 0:
        print("nem páratlan")
    else:
        nums = [ i for i in range(height+1) if i%2 == 1]
        for i in nums:
            print(" "*int((height-i)/2) + "*"*i + " "*int((height-i)/2))
        nums.remove(height)
        nums.reverse()
        for i in nums:
            print(" "*int((height-i)/2) + "*"*i + " "*int((height-i)/2))





def main():
    diamond(7)

if __name__ == "__main__":
    main()