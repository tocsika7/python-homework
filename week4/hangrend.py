MELY_MGH = 'aáoóuú'
MAGAS_MGH = 'eéiíöőüű'

MELY = 0
MAGAS = 1
VEGYES = 2

def hangrend(word):
    mely = 0
    magas = 0
    for c in word:
        if c in list(MELY_MGH):
            mely += 1
        else:
            if c in list(MAGAS_MGH):
                magas += 1

    if magas > 0 and mely > 0:
        return MAGAS
    else:
        if mely > 0: 
            return MELY
        else:
            return VEGYES

def main():
    print(hangrend('kisvasút'))
    print(hangrend('magas'))
    print(hangrend('mély'))



if __name__ == "__main__":
    main()