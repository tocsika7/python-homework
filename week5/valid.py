def valid(text, chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    validated_text = ''
    for c in text:
        if c in chars:
            validated_text += c
    
    print(validated_text)

def main():
    valid("Barking!")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")

if __name__ == "__main__":
    main()