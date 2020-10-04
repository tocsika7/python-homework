def main():

    text = """Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb"""

    print(text)
    
    t1 = "abc...ABC.."
    t2 = "cdef...zabCDE..."

    for c in text:
        pos = t1.find(c)
        if pos == -1:
            print(c, end="")
        else: 
            print(t2[pos])

if __name__ == "__main__":
    main()