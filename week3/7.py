import string

ABC = string.ascii_letters

def shift(message,offset):
    trans = str.maketrans(ABC,ABC[offset:] + ABC[:offset])
    return message.translate(trans)

def main():

    text = """Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb"""

    print(text)
    print(shift(text,2))


if __name__ == "__main__":
    main()