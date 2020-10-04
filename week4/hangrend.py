MELY = 'aáoóuú'
MAGAS = 'eéiíöőüű'

def hangrend(word):
    mely = 0
    magas = 0
    for c in word:
        if c in list(MELY):
            mely += 1
        else:
            if c in list(MAGAS):
                magas += 1

    if magas > 0 and mely > 0:
        return 'vegyes'
    else:
        if mely > 0: 
            return 'mély'
        else:
            return 'magas'

def main():
    print(hangrend('kisvasút'))



if __name__ == "__main__":
    main()