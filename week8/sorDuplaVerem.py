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

class Sor:
    
    def __init__(self):
        self.verem1 = Verem()
        self.verem2 = Verem()
        self.size = 0

    def betesz(self,value):
        self.verem1.betesz(value)
        self.size += 1

    def balrolKivesz(self):
        if self.verem1.meret() == 0: 
            return "A verem üres"
        else:
            while self.verem1.meret() != 1:
                self.verem2.betesz(self.verem1.kivesz())

            temp = self.verem1.kivesz()

            while self.verem2.meret() != 0:
                self.verem1.betesz(self.verem2.kivesz())

            return temp

    
    def meret(self):
        return self.verem1.meret()

    def ures(self):
        return self.verem1.meret() == 0

    def __str__(self):
        return str(self.verem1)

def main():
    s = Sor()
    print(s.ures())
    s.betesz(12)
    s.betesz(45)
    s.betesz(35)
    print(s)
    print(s.meret())
    s.balrolKivesz()
    s.balrolKivesz()
    print(s)
    s.balrolKivesz()
    print(s.ures())
    s.balrolKivesz()


if __name__ == "__main__":
    main()
