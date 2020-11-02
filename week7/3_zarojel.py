def isValidBrackets(text):
    li = []
    li2 = []
    
    di = {}
    di['('] = ')'
    di['['] = ']'
    di['{'] = '}'

    for c in text:
        if c in ['(', '[', '{', ')', ']', '}']:
            li.append(c)
    
    szoveg = ''.join(li)

    for c in szoveg: 
        if c in ["(", "{", "["]: 
            li2.append(c) 
        else: 
            if len(li2) == 0: 
                return False

            index = li2.pop() 

            if di[index] != c: 
                return False

    if len(li2) != 0: 
        return False
    else:
        return True
   
    
def main():
    print(isValidBrackets("((5+3)*2+1)"))
    print(isValidBrackets("{[(3+1)+2]+}"))
    print(isValidBrackets("(3+{1-1)}"))
    print(isValidBrackets("[1+1]+(2*2)-{3/3}"))
    print(isValidBrackets("(({[(((1)-2)+3)-3]/3}-3)"))
 



if __name__ == "__main__":
    main()