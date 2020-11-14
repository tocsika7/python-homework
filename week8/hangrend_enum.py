from enum import Enum, auto

MELY_MGH = 'aáoóuú'
MAGAS_MGH = 'eéiíöőüű'

class Hangrend(Enum):
    MAGAS = auto()
    MELY = auto()
    VEGYES = auto()


def milyenHangrend(word):
    mely = 0
    magas = 0
    for c in word:
        if c in list(MELY_MGH):
            mely += 1
        else:
            if c in list(MAGAS_MGH):
                magas += 1

    if magas > 0 and mely > 0:
        return (word, Hangrend.MAGAS.name,Hangrend.MAGAS.value)
    else:
        if mely > 0: 
            return (word, Hangrend.MELY.name,Hangrend.MELY.value)
        else:
            return (word, Hangrend.VEGYES.name,Hangrend.VEGYES.value)

def main():
    print(milyenHangrend('kisvasút'))
    print(milyenHangrend('magas'))
    print(milyenHangrend('mély'))



if __name__ == "__main__":
    main()