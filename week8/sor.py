class Queue:

    def __init__(self):
        self.data = []

    def betesz(self, value):
        self.data.append(value)

    def kiveszBalrol(self):
        if not self.data:
            return "Hiba a sor üres"
        else:
            return self.data.pop(0)

    def ures(self):
        return  not self.data
    
    def meret(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)

def main():
    q = Queue()
    print(q)
    q.betesz(5)
    q.betesz(32)
    print(q)
    print(q.meret())
    q.kiveszBalrol()
    print(q)
    print(q.ures())
    print(q.kiveszBalrol())

if __name__ == "__main__":
    main()
