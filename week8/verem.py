class Verem:

    def __init__(self):
        self.data = []

    def betesz(self,value):
        self.data.append(value)

    def kivesz(self):
        if not self.data:
            return "Hiba a verem üres"
        else:
            return self.data.pop()

    def ures(self):
        return  not self.data
    
    def meret(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)[:-1]

def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

if __name__ == "__main__":
    main()