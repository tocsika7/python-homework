
''' Függvény ami kap egy stringet és azokat a karaktereket adja vissza 
belőle amelyek a második paraméterként kapott stringben szerepelnek. 

@param text : string Bemeneti szöveg 
@param chars: string A karakterek amelyek meglétét az első paraméterben akarunk ellenőrizni
@return validated_text : string A karakterek az első paraméterből amelyek benne vannak a második paraméterként kapott stringben. 
'''
def valid(text, chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    validated_text = ''
    for c in text:
        if c in chars:
            validated_text += c
    
    return validated_text

def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))

if __name__ == "__main__":
    main()