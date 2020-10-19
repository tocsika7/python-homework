def replaceWordsDict(text,dict):
    for key in dict:
        text = text.replace(key, dict[key])
    return text

def replaceWords(text,original,changed):
    i = 0
    while i < len(original):
        text = text.replace(original[i],changed[i])
        i += 1
    
    return text

def main():
    d = {'á':'a','Á':'A','é':'e','É':'E','ó':'o','Ó':'O',
    'ö':'o','Ö':'O','ő':'o','Ő':'O','ú':'u','Ú':'U','ü':'u',
    'Ü':'U','ű':'u','Ű':'U','í':'i','Í':'I'}

    text = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

    A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

    A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

    print(replaceWordsDict(text,d))
    print(replaceWords(text,'áéíóöőúüűÁÉÍÓÖŐÚÜŰ',
    'aeiooouuuAEIOOOUUU'))

if __name__ == "__main__":
    main()

    