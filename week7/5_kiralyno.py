def rajzol(lista):
    print("+" + 17*"." + "+")

    text = ''.join([str(i) for i in lista])

    index = 7
    for i in range(8):
        row = text.find(str(index))
        print("| "+ row*". "+ "Q "+ (7-row)*". " + "|")
        row -= 1

    print("+"+ 17*"." + "+\n")

def main():
    rajzol([7,3,0,2,5,1,6,4])
    rajzol([0,4,7,5,2,6,1,3])

if __name__ == "__main__":
    main()