def ciklus(n,debug = False):
    if debug:
        print('# ciklus kezdete')
    for i in range(1,n+1):
        print(i,end=',')
    if debug:
        print('')
        print('# ciklus vége')
  


def main():
    ciklus(10)

if __name__ == "__main__":
    main()