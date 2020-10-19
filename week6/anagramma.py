def normalize(text):
    return text.lower().replace(' ','')

def isAnagramma(text1,text2):
    li1 = normalize(text1).split().sort()
    li2 = normalize(text2).split().sort()
    if (li1 == li2):
        return True
    else:
        return False

def isAnagramma2(text1,text2):
    text1 = normalize(text1)
    text2 = normalize(text2)
    test = {}
    if len(text1) != len(text2):
        return False
    
    for s in text1:
        if s not in test.keys():
            test[s] = 0
        test[s] += 1
    
    for s in text2:
        if s not in test.keys() or test[s] == 0:
            return False
        test[s] -= 1

    print(test)
    return True

    

    

def main():
    print(isAnagramma('listen','silent'))
    print(isAnagramma('A gentleman', 'Elegant man'))
    print(isAnagramma('Clint Eastwood', 'Old west action'))
    print(isAnagramma2('listen','silent'))
    print(isAnagramma2('A gentleman', 'Elegant man'))
    print(isAnagramma2('Clint Eastwood', 'Old west action'))

if __name__ == "__main__":
    main()