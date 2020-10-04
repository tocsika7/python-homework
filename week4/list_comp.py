def main():
    #1 
    li1 = ['auto', 'villamos', 'metro']
    li1_new = [w.upper() for w in li1]
    print(li1_new)

    #2 
    li2 = ['aladar', 'bela', 'cecil']
    li2_new = [w.capitalize() for w in li2]
    print(li2_new)

    #3 
    li3 = [0 for i in range(1,10+1)]
    print(li3)

    #4
    li4 = [i for i in range(1,10+1)]
    li4_new = [i*2 for i in li4]
    print(li4_new)

    #5
    li5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    li5_new = [int(c) for c in li5]
    print(li5_new)

    #6 
    s6 = "1234567"
    li6 = [int(c) for c in s6]
    print(li6)

    #7 
    s7 = 'The quick brown fox jumps over the lazy dog'
    li7 = [len(w) for w in s7.split()]
    print(li7)

    #8 
    s8 = "python is an awesome language"
    li8 = [c[0] for c in s8.split()]
    print(li8)

    #9 
    s9 = 'The quick brown fox jumps over the lazy dog'
    li9 = [(w,len(w)) for w in s9.split()]
    print(li9)

    #10 
    li10 = [i for i in range(0,9+1) if i % 2 == 0]
    print(li10)

    #11 
    li11 = [i*i for i in range(0,19)]
    print(li11)

    #12
    li12 = [i*i for i in range(0,19) if str(i*i)[len(str(i*i))-1] == '4']
    print(li12)

    #13 
    li13 = [chr(i) for i in range(65,90+1)]
    print("".join(li13))

    #14 
    li14 = [' apple ', ' banana ', ' kiwi'] 
    li14_new = [w.replace(" ","") for w in li14]
    print(li14_new)

    #15 
    li15 = [1, 0, 1, 1, 0, 1, 0, 0]
    li15_new = [str(i) for i in li15]
    print("".join(li15_new))


#####################################

if __name__ == "__main__":
    main()    