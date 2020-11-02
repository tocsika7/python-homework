def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord('a'), ord('z')))

    for t in list(zip([c for c in chars],codes)):
        print(t)

if __name__ == "__main__":
    main()