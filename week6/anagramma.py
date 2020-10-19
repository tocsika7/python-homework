def normalize(text):
    return text.lower().replace(' ','')

def isAnagramma(text1,text2):
    li1 = normalize(text1).split().sort()
    li2 = normalize(text2).split().sort()
    if (li1 == li2):
        return True
    else:
        return False

def main():
    print(isAnagramma('listen','silent'))
    print(isAnagramma('A gentleman', 'Elegant man'))
    print(isAnagramma('Clint Eastwood', 'Old west action'))

if __name__ == "__main__":
    main()