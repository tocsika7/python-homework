import sys

def diamond(size):

    if size % 2 != 1:
        print("Páratlan számot kell megadni")
        sys.exit()        
    i = 1
    while i < size:
        text = "*"*i
        print(text.center(size, " "), end="")
        print()
        i += 2

    while i > 0:
        text = "*"*i
        print(text.center(size, " "), end="")
        print()
        i -= 2





def main():
    diamond(11)

if __name__ == "__main__":
    main()